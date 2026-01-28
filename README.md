# Goma Social

> Oneliner: Projeto de hobby/estudo de uma *slow social media* para *gamers*.

![Status](https://img.shields.io/badge/Status-Fase%20de%20Planejamento-orange?style=for-the-badge)

## 0. Antes de tudo

Este é um projeto pessoal para estudo e desenvolvimento. O projeto não tem fins lucrativos; o foco é aprender, experimentar e criar, para quem sabe, ao final, ter uma plataforma sólida que contribua para algo maior.

## Sumário

- [1. Apresentação](#1-apresentação)
- [2. Stack de Tecnologias](#2-stack-de-tecnologias)
- [3. Estrutura do Projeto](#3-estrutura-do-projeto)
- [4. MVP](#4-mvp)
- [5. Como Rodar](#5-como-rodar)
- [6. Contribuição](#6-contribuição)

## 1. Apresentação

### O que?

Goma é uma plataforma social com grande inspiração no Orkut, que visa desacelerar e criar comunidades para o público de jogadores de jogos eletrônicos (*gamers*).

### Por que?

Goma nasce do meu descontentamento com essa constante pressão das redes sociais: notificações sem fim, a ansiedade gerada e o famoso FOMO (*fear of missing out* — medo de ficar de fora).

### Objetivo

Goma busca ser uma plataforma social de consumo lento (*slow social media*), esforçando-se para não cair nas mesmas armadilhas de outras redes sociais. Inspirada no Orkut, ela visa criar comunidades e gerar conexão. O projeto deseja evitar a constante monetização das redes e a produção de conteúdo quase exclusivamente voltada para a venda de serviços ou produtos. A comunidade é feita para compartilhar e unir, não para vender e excluir.

### O nome

Goma é uma referência direta à substância pegajosa, como na bala de goma, que dá liga às comunidades — o grude. Também é um acrônimo para *Gamers On Meeting Area*, ou seja, **jogadores em área de encontro**.

### Público alvo

- Jogadores de **PC e Consoles**
- Jogadores que valorizam comunidades duradouras sobre interações efêmeras
- Pessoas que sentem falta de um espaço social permanente para sua vida gamer

**Idioma:** Desenvolvimento inicial em **Português (BR)**.

### Pilares

A plataforma fundamenta-se em três eixos principais, denominados internamente como:

- **Comunidade (Grude):** Fóruns estruturados para acúmulo de conhecimento e discussão centralizada.
- **Identidade (Base):** Perfis ricos que exibem a trajetória e reputação do jogador.
- **Conectividade (Junção)** Ferramentas para encontrar jogadores com afinidades reais através de APIs e algoritmos sociais.

## 2. Stack de Tecnologias

| Categoria | Tecnologia e Escolha |
| ---- | ---- |
| **Backend** | **FastAPI**: Framework Python focado em performance para a construção da API |
| **Frontend** | **Nuxt.js**: Framework Vue.js (JavaScript) para uma interface reativa e otimizada (SSR/SSG) |
| **Banco de Dados** | **PostgreSQL**: Banco relacional robusto para garantir a integridade |
| **Modelagem/ORM** | **SQLAlchemy**: Tradução de objetos Python para queries SQL de forma eficiente |
| **Autenticação** | **Supabase Auth**: Gerenciamento de usuários e segurança via JWT |
| **Armazenamento** | **Supabase Storage**: Custódia de mídias (fotos de perfil e posts) |
| **Integração** | **Steam & IGDB APIs**: Conexão com bases de dados externas de jogos |

### Justificativa

Foi escolhido **FastAPI** como backend principal pela familiaridade com Python e pela flexibilidade no desenvolvimento da lógica de negócio. **Supabase** foi integrado para gerenciar autenticação de usuários e armazenamento de arquivos, aproveitando sua infraestrutura pronta e segura. Para o frontend, **Nuxt.js** foi selecionado pela estrutura bem definida que facilita o aprendizado e pelas otimizações de performance nativas do framework.

### Meu Status como Desenvolvedor (é uma métrica minha.)

Da stack escolhida, as tecnologias que me encontro com maior familiaridade são Python e FastAPI, depois o Banco de Dados e o restante não tenho muito experiencia, mas estou buscando material de estudo e pratica.

### Como funciona na prática

#### Exemplos superficiais

- Fluxo de Autenticação

``` code
1. Usuário faz login → Supabase Auth
2. Supabase retorna JWT token
3. Nuxt envia token para FastAPI em cada requisição
4. FastAPI valida o token e processa a requisição
```

- Fluxo de Upload de Imagem

``` code
1. Usuário seleciona foto de perfil no Nuxt
2. Nuxt faz upload direto para Supabase Storage
3. Supabase retorna URL da imagem
4. Nuxt envia URL para FastAPI salvar no PostgreSQL
```

### Hospedagem Inicial

- **VPS Simples:** FastAPI + Nuxt
- **DB & Auth:** Supabase

## 3. Estrutura do Projeto

Aqui está como esse repositório está ou ficará organizado.

``` bash
./
├── backend/                 # FastAPI
├── frontend/                # Nuxt.js
├── docs/                    # Documentação complementar
│   ├── compliance-e-moderacao.md
│   ├── diretrizes-e-filosofia.md
│   └── funcionalidades.md
└── README.md                # Guia principal (Nem tão breve)
```

## 4. MVP

**Equipe:** 1 desenvolvedor (projeto pessoal)

**Filosofia:** Cronograma maleável e iterativo, priorizando aprendizado e qualidade sobre velocidade.

**Proposta:** Inicialmente só vou definir a fase do MVP para entregar algo.

### Fundação

**Objetivo:** Sistema básico funcional para validar conceito

**Tarefas:**

- [ ] Setup da base (Nuxt.js + FastAPI)
- [ ] Integração com infra (VPS + Supabase)
- [ ] Sistema de autenticação (Auth)
- [ ] CRUD de Perfis (Nome, bio, 3 jogos favoritos)
- [ ] Sistema de Comunidades (Criar, entrar, listar)
- [ ] Fórum simples (Posts e respostas em comunidades)
- [ ] Deploy básico em `goma.aforja.cloud`

**Entregável:** Usuários conseguem criar perfil, entrar em comunidades e postar.

## 5. Como Rodar

> **Nota:** Em construção - As instruções de setup local serão adicionadas assim que a estrutura base do repositório for consolidada.

## 6. Contribuição

O Goma é um projeto de estudo, mas adoraria ajuda para dar liga nessa comunidade. Se você compartilha da visão de uma rede social mais lenta e saudável para gamers, ou só quer ajudar e aprender, sinta-se em casa!

### Como você pode ajudar?

- **Ideias e Discussão:** Abra uma Issue para sugerir funcionalidades que melhorem a experiência de fóruns e podemos começar uma conversa.
- **Melhorias:** Sinta-se à vontade para enviar um Pull Request com correções, melhorias na documentação ou novas funcionalidades.

---

> **Nota**: Foi utilizado o auxílio de LLMs (Gemini e Claude) no desenvolvimento deste documento.
