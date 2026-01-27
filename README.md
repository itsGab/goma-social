> **Disclaimer**: Foi utilizado o auxílio de LLMs (Gemini e Claude) no desenvolvimento deste documento.

# PROJETO: GOMA (Gamers On Meeting Area)

- **Status:** Fase de Planejamento/Roadmap
- **Natureza:** Projeto hobby e de estudo (possível expansão futura)
- **Conceito Chave:** *Slow social media* para o ecossistema gamer.

---

## 1. Apresentação

### Antes de tudo

Este é um projeto pessoal para estudo e desenvolvimento. O projeto não tem fins lucrativos; o foco é aprender, experimentar e criar, para quem sabe, ao final, ter uma plataforma sólida que contribua para algo maior.

### O que?

Goma é uma plataforma social com grande inspiração no Orkut, que visa desacelerar e criar comunidades para o público de jogadores de jogos eletrônicos (*gamers*).

### Por que?

Goma nasce do meu descontentamento com essa constante pressão das redes sociais: notificações sem fim, a ansiedade gerada e o famoso FOMO (fear of missing out — medo de ficar de fora).

### Objetivo

Goma busca ser uma plataforma social de consumo lento (slow social media), esforçando-se para não cair nas mesmas armadilhas de outras redes sociais. Inspirada no Orkut, ela visa criar comunidades e gerar conexão. O projeto deseja evitar a constante monetização das redes e a produção de conteúdo quase exclusivamente voltada para a venda de serviços ou produtos. A comunidade é feita para compartilhar e unir, não para vender e excluir.

### O nome

Goma é uma referência direta à substância pegajosa, como na bala de goma, que dá liga às comunidades — o grude. Também é um acrônimo para *Gamers On Meeting Area*, ou seja, **jogadores em área de encontro**.

### Pontos-chave

Estes são alguns dos pontos importantes - não definitivos e ainda abertos a modificações:

- Ser uma plataforma aberta
- Criar comunidades e conexão
- Para o público gamers
- Consumo devagar (slow social media)
- Ambiente saudável (tentar reduzir a ansiedade forçada por algoritmos)
- Para todos (com bom senso, respeito e que queiram contribuir)

### Público alvo

- Jogadores de **PC e Consoles** (PlayStation, Xbox, Nintendo)
- Jogadores que valorizam comunidades duradouras sobre interações efêmeras
- Pessoas que sentem falta de um espaço social permanente para sua vida gamer

**Idioma:** Desenvolvimento inicial em **Português (BR)**.

### Pilares

A plataforma fundamenta-se em três eixos principais, denominados internamente como:

- **Comunidade (Grude):** Fóruns estruturados para acúmulo de conhecimento e discussão centralizada.
- **Identidade (Base):** Perfis ricos que exibem a trajetória e reputação do jogador.
- **Conectividade (Junção)** Fe:rramentas para encontrar jogadores com afinidades reais através de APIs e algoritmos sociais.

### Glossário #TODO: colocar no final, tenho que revisar isso, complementar e colocar no final***

- **Orkut:** rede social brasileira popular nos anos 2000, focada em comunidades e perfis personalizados
- **FOMO:** sigla para *Fear of Missing Out* (medo de ficar de fora)
- **Slow social media:** movimento que propõe um consumo mais consciente e lento das redes sociais
- **Gamers:** #TODO: completar!!!

---

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

- **Backend:** FastAPI (Python) *sei um pouco*
- **Frontend:** Nuxt.js (Vue.js) *comecei a estudar*
- **Banco de Dados:** PostgreSQL *sei um pouco*
- **Autenticação:** Supabase Auth *não sei*
- **Storage:** Supabase Storage (imagens e arquivos) *não sei*
- **ORM:** SQLAlchemy *sei um pouco*
- **API Externas**: (Estudar possibilidades, e.g.:) *não sei*
  - **IGDB/RAWG API**
  - **Steam Web API**

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

# ======= RESCRITO ATÉ AQUI =======

## 6. DIRETRIZES DE DESIGN E FILOSOFIA

### 6.1. Princípios de UX

- **Ausência de DM inicial:** Para evitar a urgência, o foco inicial são os Recados (Scraps). O Discord serve como complemento para chat de voz.
- **Customização:** Skins e temas de perfil para gerar senso de posse (estilo MySpace/Orkut).
- **Gamificação não-viciante:** Sistema de badges e conquistas que recompensam participação genuína, não tempo de tela.

### 6.2. Anti-Padrões (O que NÃO faremos)

- ❌ **Notificações Push excessivas** - Evitar ansiedade e FOMO
- ❌ **Feeds algorítmicos** - Cronologia simples e transparente
- ❌ **Métricas de vaidade** - Sem contadores públicos de seguidores
- ❌ **Mecanismos de vício** - Sem streaks obrigatórias ou timers de urgência
- ❌ **Segregação por pagamento** - Funcionalidades core sempre gratuitas

---

## 7. MODELO DE SUSTENTABILIDADE

### 7.1. Fase Atual (Projeto Hobby)

**Custos cobertos pessoalmente:**

- Servidor VPS
- Domínio
- Eventuais custos de APIs

**Sem monetização ativa no curto prazo.**

### 7.2. Possibilidades Futuras (Se necessário)

**Subscription Opcional de Apoio:**

- **"Apoiador GOMA"** (~R$ 5-10/mês)
- Benefícios simbólicos: badge especial, temas exclusivos, prioridade em filas
- **Importante:** Nenhuma funcionalidade core será bloqueada para não-apoiadores

**Marketplace Comunitário (Longo Prazo):**

- Usuários criam e vendem temas/avatares customizados
- Taxa de transação (ex: 20%) para manutenção da plataforma
- 80% do valor vai para o criador
- **Requer análise cuidadosa antes de implementação**

### 7.3. Monetização Proibida

- ❌ Venda de dados de usuários
- ❌ Anúncios intrusivos ou rastreamento
- ❌ Pay-to-win em sistemas de reputação
- ❌ Itens que segreguem jogadores por poder aquisitivo

---

## 8. MÉTRICAS DE SUCESSO

Em vez de focar em números absolutos, priorizamos **satisfação e engajamento qualitativo**:

### 8.1. Indicadores Primários

- **Taxa de Retorno Semanal:** Usuários que voltam pelo menos 1x por semana
- **NPS (Net Promoter Score):** "Você recomendaria o GOMA para um amigo gamer?"
- **Tempo Médio de Permanência:** Qualidade > quantidade (sessões significativas)
- **Taxa de Perfis Completos:** % de usuários que preenchem 70%+ do perfil

### 8.2. Indicadores Secundários

- **Comunidades Ativas:** Com pelo menos 5 posts nos últimos 30 dias
- **Testemunhos Escritos:** Indicador de conexões genuínas
- **Taxa de Moderação:** Baixos reports indicam comunidade saudável

### 8.3. Anti-Métricas

**O que NÃO usaremos como sucesso:**

- Número bruto de usuários cadastrados (vanity metric)
- Tempo total gasto na plataforma (queremos qualidade, não vício)
- Daily Active Users inflados por notificações forçadas

---

## 9. ROADMAP E CRONOGRAMA

**Equipe:** 1 desenvolvedor (projeto pessoal)

**Filosofia:** Cronograma maleável e iterativo, priorizando aprendizado e qualidade sobre velocidade.

### 9.1. Fase 1 - MVP Core (Fundação)

**Objetivo:** Sistema básico funcional para validar conceito

**Tarefas:**

- [ ] Setup infraestrutura (VPS + Supabase)
- [ ] Sistema de autenticação (OAuth com Steam/Discord)
- [ ] CRUD de Perfis (Nome, bio, 3 jogos favoritos)
- [ ] Sistema de Comunidades (Criar, entrar, listar)
- [ ] Fórum simples (Posts e respostas em comunidades)
- [ ] Deploy básico em `goma.aforja.cloud`

**Entregável:** Usuários conseguem criar perfil, entrar em comunidades e postar.

**Duração Estimada:** Flexível (2-4 meses em ritmo hobby)

---

### 9.2. Fase 2 - Features Sociais (Conexão)

**Objetivo:** Adicionar camada social inspirada no Orkut

**Tarefas:**

- [ ] Mural de Recados (Scraps) sem notificações
- [ ] Sistema de Testemunhos (Depoimentos)
- [ ] Check-in de Perfil ("Deixar um GG")
- [ ] Sistema básico de Badges (Mentor, Tanker, etc.)
- [ ] Página de "Favoritos" expandida (vitrine de jogos)

**Entregável:** Usuários conseguem interagir em perfis alheios de forma assíncrona.

**Duração Estimada:** Flexível (1-3 meses)

---

### 9.3. Fase 3 - Integração Gamer (Identidade)

**Objetivo:** Conectar perfis com bibliotecas reais de jogos

**Tarefas:**

- [ ] Integração Steam API (conquistas e biblioteca)
- [ ] "Cofre de Conquistas" (top 3 conquistas destacadas)
- [ ] Widget de status (o que está jogando agora)
- [ ] Daily Buff (frase motivacional diária)

**Entregável:** Perfil reflete a jornada real do jogador.

**Duração Estimada:** Flexível (1-2 meses)

---

### 9.4. Fase 4 - Features Avançadas (Diferenciação)

**Objetivo:** Implementar funcionalidades únicas do GOMA

**Tarefas:**

- [ ] Sistema LFG (Looking for Group) básico
- [ ] Cápsula do Tempo (mensagens futuras)
- [ ] Desafios Amigáveis entre usuários
- [ ] Mini-games de tabuleiro (Xadrez/Damas)
- [ ] Sistema de customização de perfil (temas)

**Entregável:** GOMA se diferencia completamente de outras redes.

**Duração Estimada:** Flexível (2-4 meses)

---

### 9.5. Fase 5 - Lançamento Público (Estabilização)

**Objetivo:** Abrir para público geral com estabilidade

**Tarefas:**

- [ ] Polimento geral de UX/UI
- [ ] Documentação de uso (FAQ + tutoriais)
- [ ] Sistema de moderação comunitária
- [ ] Testes de carga e otimizações
- [ ] Onboarding guiado para novos usuários

**Entregável:** Plataforma pronta para crescimento orgânico.

---

**Nota sobre o cronograma:** As fases podem se sobrepor, ser reordenadas ou pausadas conforme necessidade de estudo, feedbacks ou disponibilidade pessoal. O importante é manter consistência, não velocidade.

---

## 10. RISCOS E FATORES DE INSATISFAÇÃO

**Objetivo:** Identificar o que pode fazer usuários não voltarem, sem criar dependência viciante.

### 10.1. Riscos de Abandono

| Fator de Risco | Probabilidade | Impacto | Estratégia de Mitigação |
| ---- | ---- | ---- | ---- |
| **Interface confusa** | Média | Alto | Onboarding claro + tooltips contextuais |
| **Falta de movimento inicial** | Alta | Alto | Beta fechado com comunidade seed (20-50 early adopters) |
| **Comunidades tóxicas** | Média | Crítico | Sistema de moderação comunitária + código de conduta |
| **Funcionalidades incompletas** | Alta | Médio | Comunicação transparente sobre fase de desenvolvimento |
| **Lentidão/bugs** | Média | Alto | Testes constantes + deploy gradual de features |
| **Competição com Discord/Outras** | Alta | Médio | Posicionar como **complementar**, não substituto |

### 10.2. Princípios Anti-Vício

**Como garantir que o GOMA seja saudável:**

- **Notificações Conscientes:** Somente para mensagens diretas importantes (se implementado), nunca para "puxar" o usuário
- **Sem Gamificação Coercitiva:** Badges celebram participação, não punhem ausência
- **Transparência:** Usuário vê claramente por que algo aparece no feed (sem algoritmos ocultos)
- **Controle Total:** Usuário pode desativar qualquer tipo de notificação
- **Respeito ao Tempo:** Features que funcionam de forma assíncrona (não exigem presença constante)

---

## 11. COMPLIANCE E MODERAÇÃO

### 11.1. Proteção de Dados (LGPD)

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

### 11.2. Moderação Comunitária

**Estrutura:**

- **Auto-Moderação:** Criadores de comunidades são moderadores padrão
- **Sistema de Reports:** Usuários podem reportar posts/perfis (categorias: spam, assédio, ilegal)
- **Processo de Análise:** Reports são analisados manualmente (sem ban automático)
- **Escalação:** Casos graves são encaminhados ao administrador principal

**Código de Conduta (Básico):**

1. Proibido: discurso de ódio, assédio, conteúdo ilegal, spam
2. Incentivado: respeito, colaboração, compartilhamento de conhecimento
3. Consequências: advertência → suspensão temporária → ban permanente

### 11.3. Segurança da Conta

- **Autenticação Social:** Login via Steam/Discord (Supabase OAuth)
- **Sem Senhas Armazenadas:** Delegamos auth para provedores confiáveis
- **2FA Opcional:** Pode ser implementado via Supabase no futuro
- **Sessões Seguras:** Tokens JWT com expiração

### 11.4. Propriedade Intelectual

**Posicionamento:**

- **Logos de Jogos:** Uso sob Fair Use para fins informativos (catálogo de jogos)
- **Avatares/Skins Customizados:** Usuário mantém copyright, plataforma tem licença de exibição
- **Posts/Conteúdo:** Usuário é dono, mas concede licença para exibição na plataforma

---

## 12. PRÓXIMOS PASSOS IMEDIATOS

1. **Validar Conceito:** Conversar com 5-10 gamers para validar interesse
2. **Setup Inicial:** Configurar repositório Git + ambiente de dev
3. **Prototipagem:** Criar wireframes básicos no Figma ou papel
4. **Começar MVP:** Implementar autenticação + perfil básico
5. **Documentar Aprendizados:** Manter diário de desenvolvimento para referência futura

---

## 13. CONSIDERAÇÕES FINAIS

O **GOMA** não nasce com a pretensão de ser a próxima grande rede social. É um experimento honesto para entender:

- Como criar comunidades saudáveis na era moderna?
- É possível fazer uma rede social slow em um mundo fast?
- O que os gamers realmente querem além de matchmaking?

**Sucesso neste projeto significa:**

- Aprender profundamente sobre desenvolvimento full-stack
- Criar uma comunidade pequena mas engajada
- Validar que slow-social-media tem espaço no mercado gamer
- (Bônus) Ter uma plataforma pessoal que eu mesmo quero usar

**Falha aceitável seria:**

- Descobrir que o conceito não ressoa após teste honesto
- Aprender que a manutenção é insustentável sozinho
- Perceber que Discord/outras ferramentas já resolvem o problema

O importante é documentar a jornada, aprender com os erros, e se divertir no processo. Se o GOMA crescer organicamente e demonstrar valor, ótimo. Se não, foi um laboratório valioso de aprendizado.
