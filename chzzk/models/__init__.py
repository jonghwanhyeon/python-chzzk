from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel


class Resource(BaseModel):
    url: str


class Profile(BaseModel):
    nickname: str
    image: Resource


class User(BaseModel):
    id: str
    profile: Profile
    logged_in: bool
    verified: bool


class Following(BaseModel):
    following: bool
    followed_at: Optional[datetime] = None
    notification: bool


class Channel(BaseModel):
    id: str
    type: Optional[Literal["NORMAL", "STREAMING"]] = None
    name: str
    description: Optional[str] = None
    image: Optional[Resource] = None
    verified: bool
    live: Optional[bool] = None
    followers_count: Optional[int] = None
    following: Optional[Following] = None
    blocked: Optional[bool] = None


class Video(BaseModel):
    id: str
    no: int
    title: str
    type: str
    status: Optional[str] = None
    thumbnail: Resource
    trailer: Optional[Resource] = None
    category_type: Optional[str] = None
    category: str
    published: Optional[bool] = None
    published_at: datetime
    stream_started_at: Optional[datetime] = None
    duration: int
    view_count: int
    is_paid_promotion: Optional[bool] = None
    channel: Optional[Channel] = None
