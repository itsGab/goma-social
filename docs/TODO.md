# TAREFAS ATUAIS

- [ ] Estudar para desenvolvimento do Frontend


# BACKLOG

Tarefas para depois

## BACKEND

### Endpoint ()
- [ ] **Delete User**
  - [ ] Remover acesso ao usuário ser deletado (deslogar e revogar/inválidar token)
  - [ ] QUESTÃO: Lógica de deleção! Criar campo `status` da conta e mudar para `inativo` ao invés de deletar a conta?
  - [ ] QUESTÃO: Lógica de delação (complemento): Adicionar um prazo de inatividade para a deleção 'REAL' da conta? ex.: 30 dias


### Arquitetura
- [ ] Criar **validações em models**
  - [ ] 1. Tamanho de campos
  - [ ] 2. Regras de senha
  - [ ] 3. Regex para validação de chars
- [ ] Analisar **possíveis melhorias**
  - [ ] ! Revisar se há melhorias a fazer nas chamadas de **Bancos de Dados**
  - [ ] ! Decidir criar ou não **Módulo de Chamada de Banco de Dados**
  - [ ] ! Decidir criar ou não **Módulo de Chamada de Regra de Negócios**


### Testes
- [ ] Atualizar **testes**
  - [ ] Fazer testes de regras do banco de dados
  - [ ] Fazer testes de regras de negócio
  - [ ] Adicionar o Faker para dados de teste


### Refatoração
- [ ] Estudar e aplicar **CleanCode**
  - [ ] 1. Models (singular/plural consistente)
  - [ ] 2. Funções (verbos claros)
  - [ ] 3. Variáveis (evitar nomes genéricos)
- [ ] Melhorar **mensagens de erro** e feedback
  - [ ] Tratar erros de integridade
  - [ ] Converter erros técnicos em mensagens amigáveis
  - [ ] Padronizar formato de erro (API/response)
