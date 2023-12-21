from __future__ import annotations

from datetime import datetime
from typing import Any, Generic, Literal, Optional, TypeVar

from pydantic import AliasPath, BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel

from chzzk import models as m
from chzzk.utils import to_kst

T = TypeVar("T", bound="SearchRecord")


class RawModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, extra="forbid")


class Following(RawModel):
    following: bool
    notification: bool
    follow_date: Optional[datetime] = None

    def model_post_init(self, _: Any):
        if self.follow_date is not None:
            self.follow_date = to_kst(self.follow_date)

    def wrap(self) -> m.Following:
        return m.Following(
            following=self.following,
            followed_at=self.follow_date,
            notification=self.notification,
        )


class PersonalData(RawModel):
    private_user_block: bool
    following: Optional[Following] = None


class User(RawModel):
    has_profile: bool
    user_id_hash: str
    nickname: str
    profile_image_url: str
    penalties: list[Any]
    official_noti_agree: bool
    official_noti_agree_updated_date: Optional[datetime]
    verified_mark: bool
    logged_in: bool

    def wrap(self) -> m.User:
        return m.User(
            id=self.user_id_hash,
            profile=m.Profile(
                nickname=self.nickname,
                image=m.Resource(url=self.profile_image_url),
            ),
            logged_in=self.logged_in,
            verified=self.verified_mark,
        )


class Channel(RawModel):
    channel_id: str
    channel_name: str
    channel_image_url: Optional[str] = None
    verified_mark: bool
    channel_type: Optional[Literal["NORMAL", "STREAMING"]] = None
    channel_description: Optional[str] = None
    follower_count: Optional[int] = None
    open_live: Optional[bool] = None
    personal_data: Optional[PersonalData] = None

    def wrap(self) -> m.Channel:
        following, blocked = None, None
        if self.personal_data is not None:
            if self.personal_data.following is not None:
                following = self.personal_data.following.wrap()
            blocked = self.personal_data.private_user_block

        return m.Channel(
            id=self.channel_id,
            type=self.channel_type,
            name=self.channel_name,
            description=self.channel_description,
            image=m.Resource(url=self.channel_image_url) if self.channel_image_url is not None else None,
            verified=self.verified_mark,
            live=self.open_live,
            followers_count=self.follower_count,
            following=following,
            blocked=blocked,
        )


class Video(RawModel):
    video_no: int
    video_id: str
    video_title: str
    video_type: str
    publish_date: datetime
    thumbnail_image_url: str
    trailer_url: Optional[str] = None
    duration: int
    read_count: int
    channel_id: Optional[str] = None
    publish_date_at: int
    category_type: Optional[str] = None
    video_category: str
    video_category_value: str
    exposure: Optional[bool] = None
    channel: Optional[Channel] = None
    paid_promotion: Optional[bool] = None
    in_key: Optional[str] = None
    live_open_date: Optional[datetime] = None
    vod_status: Optional[str] = None
    prev_video: Optional[Video] = None
    next_video: Optional[Video] = None

    def model_post_init(self, _: Any):
        self.publish_date = to_kst(self.publish_date)

        if self.live_open_date is not None:
            self.live_open_date = to_kst(self.live_open_date)

    def wrap(self) -> m.Video:
        return m.Video(
            id=self.video_id,
            no=self.video_no,
            title=self.video_title,
            type=self.video_type,
            status=self.vod_status,
            thumbnail=m.Resource(url=self.thumbnail_image_url),
            trailer=m.Resource(url=self.trailer_url) if self.trailer_url is not None else None,
            category_type=self.category_type,
            category=self.video_category,
            published=self.exposure,
            published_at=self.publish_date,
            stream_started_at=self.live_open_date,
            duration=self.duration,
            view_count=self.read_count,
            is_paid_promotion=self.paid_promotion,
            channel=self.channel.wrap() if self.channel is not None else None,
        )


class SearchRecord(RawModel):
    pass


class VideoSearchRecord(SearchRecord):
    video: Video
    channel: Channel


class ChannelSearchRecord(SearchRecord):
    channel: Channel


class SearchCursor(RawModel, Generic[T]):
    size: int
    next: int = Field(alias=AliasPath("page", "next", "offset"))  # type: ignore
    data: list[T]
