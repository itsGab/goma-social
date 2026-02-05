# Goma Social

> Uma *slow social media* para *gamers* inspirado no **Orkut**.

![Static Badge](https://img.shields.io/badge/planejamento-orange?style=flat&label=status)

## Sobre

Goma é uma plataforma social para jogadores de consoles e PC, que buscam comunidades e conexões reais, sem a pressão e ansiedade das redes sociais tradicionais

**O nome**: Goma representa a substância que *gruda* a comunidade. Também serve como um acrônimo para Gamers On Meeting Area (jogadores na área de encontro)

**Idioma:** Português (BR) | **Deploy:** [goma.aforja.com](https://goma.aforja.cloud)

### Por que?

- Slow Social Media: Sem notificações infinitas, evitar o FOMO, sem pressão por engajamento
- Comunidades Reais: Espaços estruturados para discussões profundas e duradouras
- Identidade Gamer: Perfis que refletem sua verdadeira trajetória como jogador
- Sem Monetização Agressiva: Foco em compartilhar, não em vender

## Stack Tecnológica

| Camada | Tecnologia |
| --- | --- |
| **Backend** | Python 3.14+, FastAPI, SQLModel (SQLAlchemy) |
| **Frontend** | *(Jinja + HTMX) / (Vue ou React)* **!EM ABERTO** |
| **Banco de Dados** | SQLite (MVP) / PostgreSQL (Escalabilidade) |
| **Autenticação** | JWT, OAuth2, pwdlib |
| **Infraestrutura** | Nginx, Supervisor, Docker |
| **Integrações** | API Steam, API IGDB |
| **Tooling** | Gerenciamento de pacotes via `uv` (Python) e `npm` (Node.js) |

## Estrutura do Projeto

``` text
./
├── backend/         # FastAPI
├── frontend/        # Vue 3
├── docs/            # Documentação complementar
└── scripts/         # Deploy e automação
```

## Roadmap MVP

### Backend
- [ ] Infraestrutura Inicial do **Backend**
  - [x] Setup do ambiente com `uv` e FastAPI.
  - [ ] Configuração de Banco de Dados Assíncrono (SQLModel + SQLAlchemy).
  - [ ] Configuração de Migrations (Alembic) com suporte a Async.
  - [ ] Configuração do ambiente de testes (Pytest).
  - [ ] Implementação do CI básico (Linter + Pytest automático).
- [ ] Gestão de Segurança e Usuário
  - [ ] Implementação de Segurança (Auth).
  - [ ] Fluxo de Autenticação (Registro/Login).
  - [ ] Testes de integração dos endpoints de segurança.
- [ ] Gestão de Dados
  - [ ] CRUD de Usuário (Perfil/Update).
  - [ ] CRUD de Post (Vinculado ao Usuário).
  - [ ] Testes de integração dos endpoints de posts.

### Frontend
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
<!-- 
### Futuro
TODO: à definir
-->

<!-- 
## Quick Start 

### Desenvolvimento Local

``` bash
TODO: atualizar assim que possível
# Backend
# Frontend
```
-->

## Contribuindo

Contribuições são bem-vindas! Se você compartilha da visão de uma rede social mais saudável para gamers:

1. Abra uma Issue para discutir ideias
2. Faça um Fork do projeto
3. Envie um Pull Request

## Status do Desenvolvedor

Este é um **projeto pessoal de estudo**. Familiaridade com as tecnologias:

- Python/FastAPI: OK
- SQL: OK
- Vue.js: Aprendendo

## Licença
<!--TODO: definir a licença-->
[A definir]
