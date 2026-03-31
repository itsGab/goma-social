# TAREFAS ATUAIS

- [ ] Estudar para desenvolvimento do Frontend


# BACKLOG

Tarefas para depois

## BACKEND

### Arquitetura
- [ ] Analisar **possíveis melhorias**
  - [ ] ! Revisar se há melhorias a fazer nas chamadas de **Bancos de Dados**
  - [ ] ! Decidir criar ou não **Módulo de Chamada de Banco de Dados**
  - [ ] ! Decidir criar ou não **Módulo de Chamada de Regra de Negócios**
- [ ] SERA????  Migrar de SQLModel para SqlAlchemy ???

### Reestruturacao
Sugestao:
```
app/
  core/
    __init__.py
    settings.py
    security.py
    exceptions.py

  services/
    __init__.py
    user.py
    post.py
    profile.py
    friendship.py
```


### Testes
- [ ] Atualizar **testes**
  - [ ] Fazer testes de regras do banco de dados
  - [ ] Fazer testes de regras de negócio
  - [ ] Adicionar o Faker para dados de teste


### Refatoração
- [ ] Reavaliar nomes
  - [ ] 1. Models (singular/plural consistente)
  - [ ] 2. Funções (verbos claros)
  - [ ] 3. Variáveis (evitar nomes genéricos)
- [ ] Melhorar **mensagens de erro** e feedback (exceptions)
  - [ ] Tratar erros de integridade
  - [ ] Converter erros técnicos em mensagens amigáveis
  - [ ] Padronizar formato de erro (API/response)
