from http import HTTPStatus

from fastapi import APIRouter, HTTPException
from sqlmodel import select

from ..database import SessionDep
from ..exceptions import ResponseMessage
from ..models import ListPosts, Post, PostInput, PostPublic
from ..security import DepCurrentUser

router = APIRouter(prefix='/post', tags=['post'])


@router.post('/create', response_model=PostPublic)
async def new_post(
    post: PostInput, session: SessionDep, current_user: DepCurrentUser
):
    if not current_user.id:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=ResponseMessage.NOT_FOUND_USER,
        )
    new_post = Post(content=post.content, user_id=current_user.id)
    session.add(new_post)
    await session.commit()
    await session.refresh(new_post)
    return new_post


@router.get('', response_model=ListPosts)
async def list_posts(session: SessionDep, current_user: DepCurrentUser):
    query = select(Post).where(Post.user_id == current_user.id)
    result = await session.execute(query)
    posts = result.scalars().all()
    return {'posts': posts}
