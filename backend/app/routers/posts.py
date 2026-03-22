from http import HTTPStatus

from fastapi import APIRouter
from sqlalchemy.orm import selectinload
from sqlmodel import and_, desc, or_, select

from ..database import SessionDep
from ..models import Friendship, ListPosts, Post, PostInput, PostPublic
from ..security import DepCurrentUser

router = APIRouter(prefix='/posts', tags=['posts'])


@router.post(
    '/create',
    response_model=PostPublic,
    status_code=HTTPStatus.CREATED,
)
async def new_post(
    post: PostInput, session: SessionDep, current_user: DepCurrentUser
):
    new_post = Post(content=post.content, user_id=current_user.id)
    session.add(new_post)
    await session.commit()
    await session.refresh(new_post)
    return new_post


@router.get('/my_posts', response_model=ListPosts)
async def list_my_posts(session: SessionDep, current_user: DepCurrentUser):
    query = select(Post).where(Post.user_id == current_user.id)
    result = await session.execute(query)
    posts = result.scalars().all()
    return {'posts': posts}


@router.get('/friends_posts', response_model=ListPosts)
async def list_friends_posts(
    session: SessionDep,
    current_user: DepCurrentUser,
):
    # TODO adicionar paginacao e ativar limit
    # limit_of_post = 100
    query = (
        select(Post)
        .options(selectinload(Post.author))
        .join(
            Friendship,
            or_(
                and_(
                    Friendship.user_id1 == current_user.id,
                    Friendship.user_id2 == Post.user_id,
                ),
                and_(
                    Friendship.user_id2 == current_user.id,
                    Friendship.user_id1 == Post.user_id,
                ),
            ),
        )
        .order_by(desc(Post.created_at))
        # .limit(limit_of_post)
    )
    result = await session.execute(query)
    posts = result.scalars().all()
    return {'posts': posts}
