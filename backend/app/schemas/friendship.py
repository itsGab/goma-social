from datetime import datetime
from enum import Enum

from pydantic import EmailStr
from sqlmodel import SQLModel


class FriendStatus(str, Enum):
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    BLOCKED = 'blocked'


class RequestType(str, Enum):
    RECEIVED = 'received'
    REQUESTED = 'requested'


class FriendRequest(SQLModel):
    friend_user_id: int
    friend_username: str
    friend_email: EmailStr
    status: FriendStatus
    created_at: datetime
    request_type: RequestType


class ListFriendRequest(SQLModel):
    pending: list[FriendRequest]


class FriendAction(str, Enum):
    ACCEPT = 'accept'
    REJECT = 'reject'


class FriendResponseInput(SQLModel):
    friend_id: int
    action: FriendAction
