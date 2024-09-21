from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

app = FastAPI()

DATABASE_URL = "postgresql://admin:admin123@postgres_db:5432/localivre"

# Configuração do banco de dados
engine = create_engine(DATABASE_URL)
metadata = MetaData()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Configuração CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite requisições de qualquer origem
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP
    allow_headers=["*"],  # Permite todos os headers
)

# Dependência para criar e fechar a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to Localivre Backend"}

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/db_test")
def db_test(db: Session = Depends(get_db)):
    try:
        # Testar a conexão com o banco de dados
        conn = engine.connect()
        return {"message": "Conexão com o banco de dados foi bem-sucedida"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conn.close()
