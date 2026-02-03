from fastapi import FastAPI

from .database import create_db_and_tables  # Importas a função aqui
from .routers import users

create_db_and_tables()

app = FastAPI()
app.include_router(users.router)


@app.get('/')
def read_root():
    return {'message': 'Hello from the backend!'}
