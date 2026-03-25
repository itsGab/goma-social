# Quick Start

No momento, apenas o ambiente de **Backend** está disponível. As instruções de **Frontend** serão atualizadas em breve conforme o progresso do desenvolvimento.


---
## Pré-requisitos

- [Docker & Docker Compose](https://docs.docker.com/engine/install/)
- [Git](https://git-scm.com/install/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [pipx](https://pipx.pypa.io/stable/installation/) (opcional, recomendado para instalar o uv)


---
## Desenvolvimento Local


### 1. Clonar o Repositório

```bash
git clone https://github.com/itsGab/goma-social.git
cd goma-social
```

### 2. **Configuração do Backend**

Entre no diretório e configure as variáveis de ambiente:


```bash
cd backend
# Copia o arquivo de exemplo para o oficial
cp .env.example .env
```
> _Avisa: Lembre-se de revisar o arquivo `.env` e alterar as credenciais caso pretenda subir para um ambiente de produção._


### 3. Instalar Dependências

Utilizando o `uv`, instale o ambiente virtual e todas as dependências (incluindo as de desenvolvimento):

```bash
uv sync --locked --all-extras --dev
```

### 4. Banco de Dados (Docker)

Para facilitar o desenvolvimento, suba um container PostgreSQL.

Comando rápido:

```docker
docker run -d \
    --name dev_db \
    -e POSTGRES_USER=app_user \
    -e POSTGRES_DB=app_db \
    -e POSTGRES_PASSWORD=app_password \
    -v pgdata_dev_db:/var/lib/postgresql/ \
    -p 5432:5432 \
    postgres:18
```

### 5. Executar a Aplicação

O comando abaixo aplica as migrações e inicia o servidor de desenvolimento:

```bash
uv run task dev
```

Para encerrar o banco de dados e liberar recursos:

```bash
uv run task db_down
# ou manualmente via docker
docker stop dev_db
```

### 6. **Configuração do Frotend**

- O ambiente de **Frontend** ainda não foi iniciado. Novas instruções serão publicadas **em breve**.
