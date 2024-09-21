# Usar uma imagem base do Python
FROM python:3.10-slim

# Instalar dependências essenciais
RUN apt-get update && apt-get install -y curl && apt-get clean

# Instalar o Poetry e adicionar ao PATH permanentemente
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    echo "export PATH=/root/.local/bin:\$PATH" >> /etc/environment

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo pyproject.toml e poetry.lock primeiro para otimizar o cache do Docker
COPY pyproject.toml poetry.lock ./

# Instalar dependências do projeto
RUN /root/.local/bin/poetry install --no-root

# Copiar o restante do código do projeto
COPY . .

# Expor a porta que será usada pelo Uvicorn
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["/root/.local/bin/poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
