> **Disclaimer**: Foi utilizado o auxílio de LLMs (Gemini e Claude) no desenvolvimento deste documento.

# PROJETO: GOMA (Gamers On Meeting Area)

- **Status:** Fase de Planejamento/Roadmap
- **Natureza:** Projeto hobby e de estudo (possível expansão futura)
- **Conceito Chave:** *Slow social media* para o ecossistema gamer.

## 1. Apresentação

### Antes de tudo

Este é um projeto pessoal para estudo e desenvolvimento. O projeto não tem fins lucrativos; o foco é aprender, experimentar e criar, para quem sabe, ao final, ter uma plataforma sólida que contribua para algo maior.

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
- **Conectividade (Junção)** Fe:rramentas para encontrar jogadores com afinidades reais através de APIs e algoritmos sociais.

## 2. Funcionalidades

### Inspiradas no Orkut

O GOMA adapta ferramentas clássicas para uma dinâmica de jogo moderna:

| Feature Orkut | Feature GOMA | Evolução / Adaptação Proposta |
| ---- | ---- | ---- |
| **Comunidades** | **Comunidades (Grude)** | Foco em fóruns assíncronos (estilo Reddit/Fórum antigo) em vez de chat linear. Permite a criação de Wikis ou Guias da comunidade. |
| **Scraps** | **Mural de Recados** | Para evitar a urgência: **sem notificação push**. O recado é um "presente" para quando o usuário logar. Pode ser usado para pedir grupo (*LFG*). |
| **Depoimentos** | **Testemunhos (Elo)** | Mantém o "Só aceita se for bom". No GOMA, isso pode contar para o nível de "Conectividade" do perfil. |
| **Buddy Poke** | **Avatar Dinâmico** | Em vez do Buddy Poke original (que era Flash), use **Sistemas de Avatares 2D/Pixel Art**. *Dica:* Integre com o **Ready Player Me** ou crie algo simples em pixel art que reflita os equipamentos do jogador. |
| **Sorte do Dia** | **Daily Buff / Quest** | Em vez de sorte, pode ser uma "Dica de Jogo do Dia" ou uma frase motivacional gamer. |
| **Visitantes** | **Check-in de Perfil** | Em vez de "dedurar" quem visitou, coloque um botão: **"Deixar um GG"**. O visitante clica se quiser avisar que passou por ali. |
| **Reputação** | **Sistema de Badges** | **Cuidado com badges negativas.** Em vez de "Rude", use a ausência de positivas ou um sistema de "Karma". Badges sugeridas: *Tanker, Healer, Shotcaller, Mentor.* |
| **Jogos** | **Mini-games de Tabuleiro** | Jogos clássicos de fórum (Xadrez, Damas, Stop) funcionam bem para criar laços enquanto se espera o download de um jogo pesado acabar. |
| **Customização** | **Temas e Skins** | Permitir mudar cores e fontes (estilo MySpace/Orkut antigo). Isso gera um senso de "posse" sobre o perfil. |

### Funcionalidades Essenciais

Estas são as funcionalidades mínimas necessárias para validar o conceito e demonstrar o valor da plataforma:

| Funcionalidade | Justificativa | Complexidade |
| ---- | ---- | ---- |
| **Autenticação** | Sem isso, não há plataforma | Baixa (Supabase) |
| **Perfil Básico** | Identidade do usuário (foto, bio, jogos favoritos) | Baixa |
| **Comunidades**| Core da proposta - criar/entrar/listar | Média |
| **Posts em Comunidades**| Interação básica dentro das comunidades | Média |
| **Mural de Recados** | Feature nostálgica que diferencia do Reddit/Discord | Baixa |
| **Sistema de Amizades**| Conexão entre usuários | Média |

### Novidades Propostas

Além das ferramentas clássicas, o projeto propõe recursos exclusivos para o público gamer:

| Nova Feature do GOMA | Proposta |
| ---- | ---- |
| **Favoritos** | Vitrine personalizada para destacar jogos, consoles e franquias favoritas do usuário. |
| **LFG (Looking for Group)** | Sistema de "Junção" onde o usuário sinaliza que quer jogar um título específico agora e busca pessoas com "Sintonia" similar. |
| **Cápsula do Tempo** | Mensagens ou prints de partidas liberados apenas após meses/anos. |
| **Desafios Amigáveis** | Amigos podem propor missões específicas (ex: "Zerar boss X") que geram medalhas de "GG" no perfil. |
| **Cofre de Conquistas** | Espaço de destaque no topo do perfil para as 3 conquistas mais difíceis do jogador (via Steam/Epic/Console). |
| **Integração de Status** | Widgets que puxam automaticamente o que o usuário está jogando via APIs externas. |

---

## 3. Stack de Tecnologias

| Categoria | Tecnologia | Escolha | Conhecimento |
| ---- | ---- | ---- | ---- |
| **Backend** | Framework Python | FastAPI | Sei um pouco |
| **Frontend** | Framework JavaScript | Nuxt.js (Vue.js) | Comecei a estudar |
| **Dados** | Banco | PostgreSQL | Sei um pouco |
| **Dados** | ORM | SQLAlchemy | Sei um pouco |
| **Infraestrutura** | Auth | Supabase Auth | Não sei |
| **Infraestrutura** | Storage | Supabase Storage | Não sei |
| **Integração** | APIs de Jogos | • IGDB/RAWG API<br>• Steam Web API | Não sei |

### Justificativa

Foi escolhido **FastAPI** como backend principal pela familiaridade com Python e pela flexibilidade no desenvolvimento da lógica de negócio. **Supabase** foi integrado para gerenciar autenticação de usuários e armazenamento de arquivos, aproveitando sua infraestrutura pronta e segura. Para o frontend, **Nuxt.js** foi selecionado pela estrutura bem definida que facilita o aprendizado e pelas otimizações de performance nativas do framework.

### Como funciona na prática

``` code
Fluxo de Autenticação

1. Usuário faz login → Supabase Auth
2. Supabase retorna JWT token
3. Nuxt envia token para FastAPI em cada requisição
4. FastAPI valida o token e processa a requisição
```

``` code
 Fluxo de Upload de Imagem

1. Usuário seleciona foto de perfil no Nuxt
2. Nuxt faz upload direto para Supabase Storage
3. Supabase retorna URL da imagem
4. Nuxt envia URL para FastAPI salvar no PostgreSQL
```

### Hospedagem Inicial

- **VPS Simples:** FastAPI + Nuxt
- **DB & Auth:** Supabase

## 4. Diretrizes e Filosofia (Sob desenvolvimento)

### Manifesto GOMA

O GOMA fundamenta-se em princípios que priorizam o bem-estar do usuário e a qualidade das interações sobre métricas de engajamento:

- **Ser uma plataforma aberta** - Código e decisões transparentes, sem algoritmos ocultos manipulando experiências.
- **Criar comunidades e conexão genuína** - Espaços duradouros onde jogadores podem construir relacionamentos reais, não apenas interações efêmeras.
- **Para o público gamer** - Entendendo as necessidades específicas de quem joga: encontrar grupos, compartilhar conquistas, discutir estratégias.
- **Consumo devagar (slow social media)** - Respeitar o tempo do usuário, sem pressão por presença constante ou FOMO artificial.
- **Ambiente saudável** - Reduzir ansiedade forçada por algoritmos, notificações excessivas e mecânicas viciantes.
- **Para todos** - Acessível a qualquer jogador que queira contribuir com bom senso e respeito, independente de poder aquisitivo.

### Princípios de Design

- **Evitar a urgência** - Nada na plataforma deve criar senso artificial de pressa. Recados aparecem quando você loga, não com notificação push. Posts não "expiram".
- **Customização** - Seu perfil é seu espaço. Temas, cores, organização - você decide como quer se apresentar.
- **Não viciante** - Features são úteis, não manipuladoras. Sem streaks obrigatórias, sem timers de urgência, sem fear of missing out.
- **Respeito** - Tanto entre usuários quanto da plataforma para com você. Seus dados são seus, seu tempo é valioso.
- **Comunidade** - O foco está em criar espaços colaborativos, não em competir por atenção ou likes.

### Anti-Padrões (O que NÃO faremos)

- **Notificações Push excessivas** - Evitar ansiedade e FOMO. Notificações apenas para mensagens diretas importantes, nunca para "puxar" o usuário de volta.
- **Feeds algorítmicos** - Cronologia simples e transparente. Você vê o que as comunidades que escolheu postam, não o que um algoritmo decide.
- **Mecanismos de vício** - Sem streaks obrigatórias, timers de urgência ou qualquer mecânica que pune você por não acessar diariamente.
- **Segregação por pagamento** - Funcionalidades core sempre gratuitas. Ninguém fica de fora por não poder pagar.
- **Monetizações proibidas:**
  - Venda de dados de usuários
  - Anúncios intrusivos ou rastreamento
  - Pay-to-win em sistemas de reputação
  - Itens que segreguem jogadores por poder aquisitivo

### Métricas de Sucesso

Em vez de focar em números absolutos, priorizamos **satisfação e engajamento qualitativo**:

- **Satisfação do Usuário** - Qualidade sobre quantidade. Medimos sessões significativas, não tempo gasto.
- **Taxa de Perfis Completos** - Percentual de usuários que preenchem 70%+ do perfil, indicando investimento real na plataforma.
- **Comunidades Ativas** - Quantidade de comunidades com pelo menos 5 posts nos últimos 30 dias.
- **Retenção Saudável** - Usuários que voltam por escolha, não por manipulação. Queremos qualidade, não vício.

### Como garantir que o GOMA seja saudável

- **Notificações Conscientes** - Somente para mensagens diretas importantes (se implementado), nunca para "puxar" o usuário.
- **Sem Gamificação Coercitiva** - Badges celebram participação, não punem ausência. Não há penalidades por ficar offline.
- **Transparência Total** - Usuário vê claramente por que algo aparece no feed. Sem algoritmos ocultos decidindo o que você vê.
- **Controle Total** - Usuário pode desativar qualquer tipo de notificação e customizar sua experiência completamente.
- **Respeito ao Tempo** - Features funcionam de forma assíncrona. Não exigem presença constante para aproveitar a plataforma.

---

## 5. Roadmap

**Equipe:** 1 desenvolvedor (projeto pessoal)

**Filosofia:** Cronograma maleável e iterativo, priorizando aprendizado e qualidade sobre velocidade.

**Proposta:** Inicialmente só vou definir a fase do MVP para entregar algo.

### Fase 1 - MVP Core (Fundação)

**Objetivo:** Sistema básico funcional para validar conceito

**Tarefas:**

- [ ] Setup da base (Nuxt.js + FastAPI)
- [ ] Integração com infraestrutura (VPS + Supabase)
- [ ] Sistema de autenticação (OAuth)
- [ ] CRUD de Perfis (Nome, bio, 3 jogos favoritos)
- [ ] Sistema de Comunidades (Criar, entrar, listar)
- [ ] Fórum simples (Posts e respostas em comunidades)
- [ ] Deploy básico em `goma.aforja.cloud`

**Entregável:** Usuários conseguem criar perfil, entrar em comunidades e postar.

## 6. Compliance e Moderação

### Proteção de Dados (LGPD)

**Compromissos:**

- **Consentimento Explícito:** Usuário sabe exatamente quais dados coletamos
- **Minimização:** Coletamos apenas o necessário (perfil público + email)
- **Portabilidade:** Usuário pode exportar todos os seus dados em JSON
- **Direito ao Esquecimento:** Deletar conta remove permanentemente dados pessoais (mantém posts anonimizados)
- **Sem Venda de Dados:** Dados nunca serão compartilhados com terceiros

**Dados Coletados:**

- Email (para login)
- Nome público e bio (visível para outros)
- Estatísticas de jogo (se usuário optar por integração)
- Posts e interações públicas em comunidades

### Moderação Comunitária

**Estrutura:**

- **Auto-Moderação:** Criadores de comunidades são moderadores padrão
- **Sistema de Reports:** Usuários podem reportar posts/perfis (categorias: spam, assédio, ilegal)
- **Processo de Análise:** Reports são analisados manualmente (sem ban automático)
- **Escalação:** Casos graves são encaminhados ao administrador principal

**Código de Conduta (Básico):**

1. Proibido: discurso de ódio, assédio, conteúdo ilegal, spam
2. Incentivado: respeito, colaboração, compartilhamento de conhecimento
3. Consequências: advertência → suspensão temporária → ban permanente

### Segurança da Conta

- **Autenticação Social:** Login via Steam/Discord (Supabase OAuth)
- **Sem Senhas Armazenadas:** Delegamos auth para provedores confiáveis
- **2FA Opcional:** Pode ser implementado via Supabase no futuro
- **Sessões Seguras:** Tokens JWT com expiração

### Propriedade Intelectual

**Posicionamento:**

- **Logos de Jogos:** Uso sob Fair Use para fins informativos (catálogo de jogos)
- **Avatares/Skins Customizados:** Usuário mantém copyright, plataforma tem licença de exibição
- **Posts/Conteúdo:** Usuário é dono, mas concede licença para exibição na plataforma
