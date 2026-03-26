Anotar as próximas tarefas aqui:

> **Nota**: Estou pensando em simplificar o projeto, não sei se estou satisfeito com o escopo. Por ser um projeto de estudo acho que ele está com muitas ideias: "*vuu ser u orkuti di gamis, nhe-nhe-nhe*".


# GERAL

## Tarefa Atual
- [ ] Resolver e não adicionar novas tarefas no BACKEND
- [ ] Começar a desenvolver o FRONTEND


# DOCUMENTAÇÃO

## OK


# BACKEND

## Endpoint
- [ ] Friend Requests
  - [ ] Mudar a listagem de pedidos de amizade, listar todos os request pending enviados ou recebidos pelo usuario ao invés de apenas os recebidos.
- [x] Posts
  - [x] Criar listagem de post de amigos
- [ ] REVISÃO:
  - [ ] Verificar se as chamadas de banco de dados nos endpoints estão usando poderiam usar o union para pegar relação de amigos, assim comom esta sendo feito no `/friends_posts`.

## Testes
- [ ] Atualizar testes
  - [ ] Fazer testes de regras do banco de dados
  - [ ] Fazer testes de regras de negócio
  - [ ] Adicionar o Faker para dados de teste

## Refatoração
- [ ] DECIDIR SE: Vale a pena pesquisar CleanCode?
- [ ] Padronizar nomenclatura
  - [ ] 1. Models (singular/plural consistente)
  - [ ] 2. Funções (verbos claros)
  - [ ] 3. Variáveis (evitar nomes genéricos)

## Domínio e validações
- [ ] Criar validações nos models
  - [ ] 1. Tamanho de campos
  - [ ] 2. Regras de senha
  - [ ] 3. Regex para validação de chars
- [ ] Mapear regras de negócio existentes
- [ ] Decidir organização ENTRE:
  - [ ] Manter simples → dentro dos models
  - [ ] Complexas → extrair para módulo (services/domain)

## Erros e feedback
- [ ] Melhorar mensagens de erro
  - [ ] Tratar erros de integridade
  - [ ] Converter erros técnicos em mensagens amigáveis
  - [ ] Padronizar formato de erro (API/response)


# FRONTEND

## Sem tarefas no momento.


# BACKLOG

## Endpoint
- [ ] **Delete User**
  - [ ] Remover acesso ao usuário ser deletado (deslogar e revogar/inválidar token)
  - [ ] QUESTÃO: Lógica de deleção! Criar campo `status` da conta e mudar para `inativo` ao invés de deletar a conta?
  - [ ] QUESTÃO: Lógica de delação (complemento): Adicionar um prazo de inatividade para a deleção 'REAL' da conta? ex.: 30 dias
