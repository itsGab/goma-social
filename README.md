# Goma Social

> Uma *slow social media* para *gamers* inspirado no **Orkut**.

![Static Badge](https://img.shields.io/badge/indo_aos_poucos-orange?style=flat&label=status)

---

## Sobre

Goma é um projeto pessoal de uma rede social para gamers que buscam comunidades e conexões reais, sem a pressão e ansiedade das redes sociais tradicionais.

### Principíos

- Slow Social Media: Sem notificações infinitas, evitar o FOMO, sem pressão por engajamento
- Comunidades Reais: Espaços estruturados para discussões profundas e duradouras
- Identidade Gamer: Perfis que refletem sua verdadeira trajetória como jogador
- Sem Monetização Agressiva: Foco em compartilhar, não em vender
---

## Stack

### Tecnologias

| Camada | Tecnologia |
| --- | --- |
| **Backend** | Python 3.14+, FastAPI, SQLModel (SQLAlchemy) |
| **Frontend** | **EM ABERTO!**: A princípio *JavaScript* |
| **Banco de Dados** | SQLite (MVP) / PostgreSQL |
| **Autenticação** | JWT, OAuth2, pwdlib |
| **Infraestrutura** | Nginx, Docker |
| **Integrações** | API Steam, API IGDB |
| **Tooling** | Gerenciamento de pacotes via `uv` (Python) |

### Estrutura do Projeto

``` text
./
├── backend/         # FastAPI
├── frontend/        # Frontend (JavaScript)
├── docs/            # Documentação complementar
└── scripts/         # Deploy e automação
```
---

## Roadmap Atual

### Backend

- [x] Infraestrutura Inicial do **Backend**
- [x] Gestão Inicial de Segurança e Usuário
- [ ] Gestão Inicial de Dados
  - [x] CRUD de Usuário (Perfil/Update).
  - [x] CRUD de Post (Vinculado ao Usuário).
  - [ ] Testes de integração dos endpoints de posts.
- [ ] ...

Acesse o [roadmap completo](./docs/roadmap-completo.md)

---

## Contribuindo

Contribuições são bem-vindas! Se você compartilha da visão de uma rede social mais saudável para gamers:

1. Abra uma Issue para discutir ideias
2. Faça um Fork do projeto
3. Envie um Pull Request

### Quick Start

No momento, apenas o ambiente de **backend** está disponível para configuração. As instruções de **frontend** serão disponibilizadas conforme o progresso do desenvolvimento.

[Instruções de como clonar e configurar o ambiente de desenvolvimento do projeto](./docs/quick-start-dev.md).

## Licença
<!--TODO: definir a licença-->
[A definir]
