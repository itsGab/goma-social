# Goma Social

> Uma *slow social media* para *gamers* inspirado no **Orkut**.

![Static Badge](https://img.shields.io/badge/planejamento-orange?style=flat&label=status)

## Sobre

Goma é uma plataforma social para jogadores de consoles e PC, que buscam comunidades e conexões reais, sem a pressão e ansiedade das redes sociais tradicionais

**O nome**: Goma representa a substância que *gruda* a comunidade. Também serve como um acrônimo para Gamers On Meeting Area (jogadores na área de encontro)

**Idioma:** Português (BR)

### Por que?

- Slow Social Media: Sem notificações infinitas, evitar o FOMO, sem pressão por engajamento
- Comunidades Reais: Espaços estruturados para discussões profundas e duradouras
- Identidade Gamer: Perfis que refletem sua verdadeira trajetória como jogador
- Sem Monetização Agressiva: Foco em compartilhar, não em vender

## Stack Tecnológica

| Camada | Tecnologia |
| --- | --- |
| **Backend** | Python 3.14+, FastAPI, SQLModel (SQLAlchemy) |
| **Frontend** | A princípio *JavaScript*, mas **EM ABERTO!** |
| **Banco de Dados** | SQLite (MVP) / PostgreSQL (Escalabilidade) |
| **Autenticação** | JWT, OAuth2, pwdlib |
| **Infraestrutura** | Nginx, Supervisor, Docker |
| **Integrações** | API Steam, API IGDB |
| **Tooling** | Gerenciamento de pacotes via `uv` (Python) e `npm` (Node.js) |

## Estrutura do Projeto

``` text
./
├── backend/         # FastAPI
├── frontend/        # Frontend (JavaScript)
├── docs/            # Documentação complementar
└── scripts/         # Deploy e automação
```

## Roadmap MVP

### Backend
- [x] Infraestrutura Inicial do **Backend**
  - [x] Setup do ambiente com `uv` e FastAPI.
  - [x] Configuração de Banco de Dados Assíncrono (SQLModel + SQLAlchemy).
  - [x] Configuração de Migrations (Alembic) com suporte a Async.
  - [x] Configuração do ambiente de testes (Pytest).
  - [x] Implementação do CI básico (Linter + Pytest automático).
- [x] Gestão de Segurança e Usuário
  - [x] Implementação de Segurança (Auth).
  - [x] Fluxo de Autenticação (Registro/Login).
  - [x] Testes de integração dos endpoints de segurança.
- [ ] Gestão de Dados
  - [x] CRUD de Usuário (Perfil/Update).
  - [ ] CRUD de Post (Vinculado ao Usuário).
  - [ ] Testes de integração dos endpoints de posts.
- [ ] Revisão Segurança (Auth)
  - [ ] ...

### Frontend
- [ ] Estudar JavaScript
  - [ ] Curso [The Odin Project](https://www.theodinproject.com/)
- [ ] Interface Base, **Frontend**
  - [ ] Estrutura do App (*Decisão de Stack*)
  - [ ] ...

### Integração & Fullstack
- [ ] Telas e Integração (User Experience)
  - [ ] Desenvolvimento da Landing Page e Login/Registro.
  - [ ] Desenvolvimento do Feed e Perfil de Usuário.
- [ ] Expansão Social (Módulo de Comunidades)
  - [ ] Modelagem de dados para Fóruns e Respostas (Backend).
  - [ ] Endpoints de interação social (Comentários).
  - [ ] Interface de interação das comunidades (Frontend).
  - [ ] Testes de lógica das comunidades.

### Futuro 

À definir


## Quick Start 

- Clona o repositório: 
  ``` bash
  git clone https://github.com/itsGab/goma-social.git
  ```

## Desenvolvimento Local

### Backend

1. **Entre na pasta do backend:**
    ```bash
    cd backend
    ```

2. **Configure o `.env` (copie o exemplo):**
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
    uv python install 3.14
    uv sync --locked --all-extras --dev
    ```


5. **Rode a aplicação:**
    ```bash
    uv run task run
    ```

### Frontend

- *Ainda não foi desenvolvido!!!*

## Contribuindo

Contribuições são bem-vindas! Se você compartilha da visão de uma rede social mais saudável para gamers:

1. Abra uma Issue para discutir ideias
2. Faça um Fork do projeto
3. Envie um Pull Request

## Status do Desenvolvedor

Este é um **projeto pessoal de estudo**. Familiaridade com as tecnologias:

- Python/FastAPI: OK
- SQL: OK
- Frontend: ???
## Licença
<!--TODO: definir a licença-->
[A definir]
