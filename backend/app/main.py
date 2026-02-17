from fastapi import FastAPI

from .routers import auth, post, users

app = FastAPI()
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(post.router)


@app.get('/')
def read_root():
    return {'message': 'Hello from the backend!'}
