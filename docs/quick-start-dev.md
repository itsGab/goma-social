# Quick Start 

No momento, apenas o ambiente de **backend** está disponível para configuração. As instruções de **frontend** serão disponibilizadas conforme o progresso do desenvolvimento.

---

# Desenvolvimento Local

## Clone

- **Clona o repositório**: 
``` bash
git clone https://github.com/itsGab/goma-social.git cd goma-social
```

## Backend

1. **Entre na pasta do backend:**

```bash
cd backend
```

2. **Configure o `.env` (copie o exemplo):**

_Importante mudar as variáveis de ambiente para produção_
- Linux/macOS: 
```bash
cp .env.example .env
```
- Windows (PowerShell):
```bash
copy .env.example .env
```

3. **Instale as ferramentas necessárias:**

- [pipx](https://pipx.pypa.io/stable/installation/) (opcional, para instalar o uv)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

```bash
pipx install uv
```

4. **Prepare o ambiente e dependências:**

```bash
uv sync --locked --all-extras --dev
```

5. **Rode a migração do banco de dados:**

```bash
uv run alembic upgrade head
```

6. **Rode a aplicação:**

```bash
uv run task run
```

## Frontend

- O ambiente de **frontend** ainda não foi iniciado. Novas instruções serão publicadas **em breve**.
