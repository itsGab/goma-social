from fastapi import FastAPI

from .routers import auth, friends, posts, profiles, users

app = FastAPI()
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(profiles.router)
app.include_router(posts.router)
app.include_router(friends.router)


@app.get('/')
def read_root():
    return {'message': 'Hello from the backend!'}
