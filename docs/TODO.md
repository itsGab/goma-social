# TAREFAS ATUAIS

- [ ] Estudar para desenvolvimento do Frontend


# BACKLOG

Tarefas para depois

## BACKEND

### Arquitetura
- [ ] **MODELS**
  - [ ] Dividir em: Models, Schemas, Contants e Validators
  - [ ] Refatorar: substituir por contantes aonda seja apropriado
- [ ] Migrar de SQLModel para SqlAlchemy
- [ ] Analisar **possíveis melhorias**
  - [ ] ! Revisar se há melhorias a fazer nas chamadas de **Bancos de Dados**
  - [ ] ! Decidir criar ou não **Módulo de Chamada de Banco de Dados**
  - [ ] ! Decidir criar ou não **Módulo de Chamada de Regra de Negócios**

### Reestruturacao

Sugestao:
```
app/
  core/
    __init__.py
    settings.py
    security.py

  models.py

  schemas/
    __init__.py
    user.py
    post.py
    profile.py

  services/
    __init__.py
    user.py
    post.py
    profile.py
    friendship.py

  constants.py
  validators.py

  routers/
    __init__.py
    auth.py
    user.py
    post.py
    profile.py
    friendship.py

  database.py
  main.py
```


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
