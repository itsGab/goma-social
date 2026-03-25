# Minha Colinha Dockers de Desenvolvimento Local

## Montar imagem `dev_db`

```bash
docker run -d \
    --name dev_db \
    -e POSTGRES_USER=app_user \
    -e POSTGRES_DB=app_db \
    -e POSTGRES_PASSWORD=app_password \
    -v pgdata_dev_db:/var/lib/postgresql/ \
    -p 5432:5432 \
    postgres:18
```

## Rodar `dev_db`

`docker start dev_db
`
## Comandos complementares com **taskipy**

```bash
run = 'uv run fastapi dev app/main.py'
migrate = 'uv run alembic upgrade head'
db_up = 'docker start dev_db'
dev = 'task db_up && task migrate && task run'
db_down = 'docker stop dev_db'
```

