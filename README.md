# PROJETO: GOMA (Gamers On Meeting Area)

> Disclaimer: Este documento foi produzido com o auxílio de LLMs e revisado e alterado por um humano.

**Status:** Fase de Planejamento/Roadmap

**Infraestrutura:** A Forja (`aforja.cloud`)

**Conceito Chave:** *Slow-social-media* para o ecossistema gamer.

---

## 1. RESUMO EXECUTIVO

O **GOMA** é uma plataforma de convivência social projetada para resgatar a essência das comunidades assíncronas (inspirada no Orkut) e adaptá-la ao contexto gamer moderno. Diferente das redes sociais atuais focadas em algoritmos e consumo rápido, o GOMA prioriza conexões duradouras, organização coletiva e a construção de uma identidade sólida dentro de um ambiente saudável.

## 2. ANÁLISE DO CENÁRIO (O Problema)

A proposta identifica três dores principais no mercado atual de jogos:

* **Fragmentação:** Jogadores dispersos sem um espaço de "convivência permanente".
* **Toxicidade:** Redes que priorizam conflitos e consumo passivo em vez de auxílio mútuo.
* **Solidão Gamer:** Falta de um "elo" social para compartilhar experiências, apesar da posse de hardware e jogos.

## 3. PILARES ESTRATÉGICOS (A Solução)

A plataforma fundamenta-se em três eixos principais, denominados internamente como:

* **Comunidade (Grude):** Fóruns estruturados para acúmulo de conhecimento e discussão centralizada.
* **Identidade (Base):** Perfis ricos que exibem a trajetória e reputação do jogador.
* **Conectividade (Junção):** Ferramentas para encontrar jogadores com afinidades reais através de APIs e algoritmos sociais.

---

## 4. ESTRUTURA DE FUNCIONALIDADES (O "Novo Orkut" Gamer)

### 4.1. Inspiradas no Orkut

O GOMA adapta ferramentas clássicas para uma dinâmica de jogo moderna:

| Feature Orkut | Feature GOMA | Evolução / Adaptação Proposta |
| --- | --- | --- |
| **Comunidades** | **Comunidades (Grude)** | Foco em fóruns assíncronos (estilo Reddit/Fórum antigo) em vez de chat linear. Permite a criação de Wikis ou Guias da comunidade. |
| **Scraps** | **Mural de Recados** | Para evitar a urgência: **sem notificação push**. O recado é um "presente" para quando o usuário logar. Pode ser usado para pedir grupo (*LFG*). |
| **Depoimentos** | **Testemunhos (Elo)** | Mantém o "Só aceita se for bom". No GOMA, isso pode contar para o nível de "Conectividade" do perfil. |
| **Buddy Poke** | **Avatar Dinâmico** | Em vez do Buddy Poke original (que era Flash), use **Sistemas de Avatares 2D/Pixel Art**. *Dica:* Integre com o **Ready Player Me** ou crie algo simples em pixel art que reflita os equipamentos do jogador. |
| **Sorte do Dia** | **Daily Buff / Quest** | Em vez de sorte, pode ser uma "Dica de Jogo do Dia" ou uma frase motivacional gamer. |
| **Visitantes** | **Check-in de Perfil** | Em vez de "dedurar" quem visitou, coloque um botão: **"Deixar um GG"**. O visitante clica se quiser avisar que passou por ali. |
| **Reputação** | **Sistema de Badges** | **Cuidado com badges negativas.** Em vez de "Rude", use a ausência de positivas ou um sistema de "Karma". Badges sugeridas: *Tanker, Healer, Shotcaller, Mentor.* |
| **Jogos** | **Mini-games de Tabuleiro** | Jogos clássicos de fórum (Xadrez, Damas, Stop) funcionam bem para criar laços enquanto se espera o download de um jogo pesado acabar. |
| **Customização** | **Temas e Skins** | Permitir mudar cores e fontes (estilo MySpace/Orkut antigo). Isso gera um senso de "posse" sobre o perfil. |

### 4.2. Prposta de Novidades

Além das ferramentas clássicas, o projeto propoem recursos exclusivos para o público gamer:

| Nova Feature do GOMA | Proposta |
| --- | --- |
| **Favoritos** | Vitrine personalizada para destacar jogos, consoles e franquias favoritas do usuário. |
| **LFG (Looking for Group)** | Sistema de "Junção" onde o usuário sinaliza que quer jogar um título específico agora e busca pessoas com "Sintonia" similar. |
| **Cápsula do Tempo** | Mensagens ou prints de partidas liberados apenas após meses/anos. |
| **Desafios Amigáveis** | Amigos podem propor missões específicas (ex: "Zerar boss X") que geram medalhas de "GG" no perfil. |
| **Cofre de Conquistas** | Espaço de destaque no topo do perfil para as 3 conquistas mais difíceis do jogador (via Steam/Epic/Console). |
| **Integração de Status** | Widgets que puxam automaticamente o que o usuário está jogando via APIs externas. |

## 5. STACK TECNOLÓGICA (A Arquitetura)

Para garantir escalabilidade, rapidez e uma experiência de usuário fluida (SPA), a arquitetura do GOMA será baseada em tecnologias modernas de alto desempenho:

* **Front-end:** **Nuxt 3 (Vue.js)**. Escolhido pela capacidade de renderização híbrida (SSR/Static), garantindo que perfis e fóruns sejam indexáveis por buscadores (SEO) e rápidos no carregamento.
* **Back-end:** **FastAPI (Python)**. Framework de alta performance para processamento de lógica de negócio, algoritmos de "Sintonia" entre jogadores e integração de dados.
* **Banco de Dados & Auth:** **Supabase (PostgreSQL)**. Utilizado para gestão de usuários, autenticação social e armazenamento relacional de comunidades e posts.
* **Storage (Imagens/Assets):** **Supabase Storage**. Armazenamento de avatares, banners de comunidades e capturas de tela (screenshots) dos usuários.
* **Integrações Externas:** * **IGDB/RAWG API:** Para catálogo de jogos.
* **Steam Web API:** Para sincronização de conquistas e bibliotecas.

## 6. DIRETRIZES DE DESIGN E MONETIZAÇÃO

* **Ausência de DM inicial:** Para evitar a urgência, o foco inicial são os Recados (Scraps). O Discord serve como complemento para chat de voz.
* **Customização:** Skins e temas de perfil para gerar senso de posse (estilo MySpace/Orkut).
* **Gamificação não-monetária:** Itens de avatar desbloqueáveis por conquistas dentro da rede, incentivando a exploração sem custo financeiro imediato.

## 7. CRONOGRAMA DE LANÇAMENTO (Roadmap)

1. **Fase Alfa:** Desenvolvimento do núcleo (perfis e comunidades).
2. **Fase Beta:** Testes com comunidades parceiras e feedback de UX.
3. **Lançamento:** Ativação oficial no domínio `goma.aforja.cloud`.
