from http import HTTPStatus

from fastapi import APIRouter

# from sqlalchemy.orm import selectinload
from sqlmodel import desc, select

from ..database import DepDBSession
from ..models import Friendship, Post
from ..schemas import ListPosts, PostInput, PostPublic, QueryPage
from ..security import DepCurrentUser

router = APIRouter(prefix='/posts', tags=['posts'])


@router.post(
    '/create',
    response_model=PostPublic,
    status_code=HTTPStatus.CREATED,
)
async def new_post(
    post: PostInput, session: DepDBSession, current_user: DepCurrentUser
):
    new_post = Post(content=post.content, user_id=current_user.id)
    session.add(new_post)
    await session.commit()
    await session.refresh(new_post)
    return new_post


@router.get('/my_posts/', response_model=ListPosts)
async def list_my_posts(
    session: DepDBSession,
    current_user: DepCurrentUser,
    page: QueryPage,
):
    query = (
        select(Post)
        .where(Post.user_id == current_user.id)
        # .options(selectinload(Post.author))
        .order_by(desc(Post.created_at))
        .limit(page.limit)
        .offset(page.offset)
    )
    result = await session.execute(query)
    posts = result.scalars().all()
    return {
        'posts': posts,
        'limit': page.limit,
        'offset': page.offset,
    }


@router.get('/friends_posts/', response_model=ListPosts)
async def list_friends_posts(
    session: DepDBSession,
    current_user: DepCurrentUser,
    page: QueryPage,
):
    friends_ids_subquery = (
        select(Friendship.user_id2)
        .where(Friendship.user_id1 == current_user.id)
        .union(
            select(Friendship.user_id1).where(
                Friendship.user_id2 == current_user.id
            )
        )
    )
    query = (
        select(Post)
        .where(Post.user_id.in_(friends_ids_subquery))
        # .options(selectinload(Post.author))
        .order_by(desc(Post.created_at))
        .limit(page.limit)
        .offset(page.offset)
    )
    result = await session.execute(query)
    posts = result.scalars().all()

    return {
        'posts': posts,
        'limit': page.limit,
        'offset': page.offset,
    }
