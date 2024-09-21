Aqui está um modelo de README perfeito para o projeto *Localivre*:

---

# Localivre 📚

Localivre é um sistema para gerenciamento de bibliotecas, com a capacidade de realizar operações de cadastro e consulta de livros. Ele é composto por um backend em Python com FastAPI, um frontend em SvelteKit, e integrações com PostgreSQL e Kong Gateway.

## Stack Principal:

- **Backend**: Python + FastAPI
- **Frontend**: SvelteKit + Yarn
- **Banco de Dados**: PostgreSQL
- **API Gateway**: Kong
- **Gerenciamento**: Docker & Docker Compose

## Como rodar o projeto? 🚀

### Pré-requisitos:
- **Docker** e **Docker Compose** instalados.

### Instruções:

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/vkdevopsbr/localivre.git
   cd localivre
   ```

2. **Configure as variáveis de ambiente**:
   - As variáveis de ambiente estão definidas no arquivo `.env` na raiz do projeto.

3. **Iniciar os serviços**:

   Utilize os comandos abaixo em sequência para iniciar os serviços. Irá subir o banco de dados, backend, Kong e frontend.

   ```bash
    docker compose -f banco-compose.yml up -d --build
    docker compose -f back-compose.yml up -d --build
    docker compose -f kong-compose.yml up -d --build
    docker compose -f front-compose.yml up -d --build
   ```

   Isso irá:
   - Subir o banco de dados PostgreSQL e o PgAdmin.
   - Subir o backend FastAPI.
   - Subir o Kong Gateway.
   - Subir o frontend SvelteKit.

4. **Acessar o frontend**:

   Após a inicialização, o frontend estará disponível em:
   - **Frontend**: [http://localhost:3000](http://localhost:3000)

   O frontend já está configurado para se comunicar com o Kong e acessar as APIs do backend.

5. **Parar os serviços**:

   Para parar todos os serviços e remover os containers, basta executar:

   ```bash
    docker compose -f banco-compose.yml down
    docker compose -f back-compose.yml down
    docker compose -f kong-compose.yml down
    docker compose -f front-compose.yml down
   ```

## Estrutura do Projeto:

```bash
localivre/
├── backend/                   # Backend FastAPI
│   ├── app/
│   │   └── main.py             # Endpoints e conexão com o banco de dados
│   ├── Dockerfile              # Dockerfile para o backend
│   ├── pyproject.toml          # Configurações do Poetry
│   └── poetry.lock             # Dependências
├── frontend/                  # Frontend SvelteKit
│   ├── src/
│   │   ├── lib/                # Funções auxiliares
│   │   ├── routes/             # Páginas do frontend
│   │   └── app.html
│   ├── Dockerfile              # Dockerfile para o frontend
│   └── yarn.lock               # Dependências
├── banco-compose.yml           # Docker Compose do banco de dados e PgAdmin
├── back-compose.yml            # Docker Compose do backend
├── kong-compose.yml            # Docker Compose do Kong Gateway
├── front-compose.yml           # Docker Compose do frontend
├── app                         # Script para start/stop/test do projeto
└── .env                        # Variáveis de ambiente
```

## Endpoints principais do Backend:

- **Raiz**: `GET /`
  - Testa se o backend está rodando.
- **Ping**: `GET /ping`
  - Retorna uma resposta `pong` para testar a conectividade.
- **Teste do Banco**: `GET /db_test`
  - Testa a conexão com o banco de dados PostgreSQL.

## Integração com Kong Gateway:

O Kong Gateway é utilizado como proxy para gerenciar as chamadas de API. Durante a inicialização, os serviços e rotas são automaticamente registrados no Kong para gerenciar os seguintes endpoints:

- `/localivre-backend/`: Proxy para o backend.
- `/localivre-ping/`: Proxy para o endpoint `/ping`.
- `/localivre-db_test/`: Proxy para o teste de conexão com o banco.

## Ferramentas de Desenvolvimento:

- **Poetry**: Gerenciador de dependências Python.
- **Yarn**: Gerenciador de pacotes para o frontend.
- **Docker Compose**: Orquestra os containers dos serviços.

## Próximos Passos:

- irei continuar envoluindo o projeto e aprendendo novas tecnologias

## Contribuição:

Sinta-se à vontade para enviar pull requests e abrir issues com sugestões ou melhorias.

---