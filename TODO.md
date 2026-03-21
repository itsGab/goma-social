Anotar as próximas tarefas aqui:

> **Nota**: Estou pensando em simplificar o projeto, não sei se estou satisfeito com o escopo. Por ser um projeto de estudo acho que ele está com muitas ideias: "*vuu ser u orkuti di gamis, nhe-nhe-nhe*".

# DOCUMENTS

## Atualizações
- [ ] Atualizar o `quick-start-dev.md` (add: Docker)


# BACKEND

## Endpoint
- O QUE AINDA FALTA???
- [ ] Delete User
  - [ ] ??? Remover o pedido para usuário e senha ao deletar
  - [ ] Remover acesso ao usuário deletado (deslogar e invalidar token)
- [ ] Friend Requests
  - [ ] Listar todos os request pending enviados ou recebidos pelo usuario
- [ ] Posts
  - [ ] Criar listagem de post de amigos

## Testes
- [ ] Atualizar testes
  - [x] Migrar testes para PostgreSQL
  - [ ] Fazer testes de regras do banco de dados
  - [ ] Fazer testes de regras de negócio

## Refatoração
- [ ] Padronizar nomenclatura
  - [ ] Vale a pena pesquisar CleanCode?
  - [ ] Models (singular/plural consistente)
  - [ ] Funções (verbos claros)
  - [ ] Variáveis (evitar nomes genéricos)

## Domínio e validações
- [ ] Criar validações nos models
  - [ ] Tamanho de campos
  - [ ] Regras de senha
- [ ] Mapear regras de negócio existentes
- [ ] Decidir organização:
  - [ ] Manter simples → dentro dos models
  - [ ] Complexas → extrair para módulo (services/domain)

## Erros e feedback
- [ ] Melhorar mensagens de erro
  - [ ] Tratar erros de integridade
  - [ ] Converter erros técnicos em mensagens amigáveis
  - [ ] Padronizar formato de erro (API/response)


# FRONTEND

## Sem tarefas no momento.
