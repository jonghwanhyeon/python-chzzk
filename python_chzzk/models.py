from __future__ import annotations

from datetime import datetime
from typing import Annotated, Any, Generic, Optional, TypeVar, Union

from pydantic import AfterValidator, BaseModel, ConfigDict, Field, Json
from pydantic.alias_generators import to_camel

from python_chzzk.utils import as_kst, to_kst

T = TypeVar("T", bound="SearchRecord")


class RawModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        frozen=True,
        extra="forbid",
    )


class User(RawModel):
    has_profile: bool
    user_id_hash: Optional[str] = None
    nickname: Optional[str] = None
    profile_image_url: Optional[str] = None
    penalties: Optional[list[Any]] = None
    official_noti_agree: bool
    official_noti_agree_updated_date: Optional[str] = None
    verified_mark: bool
    logged_in: bool


class Following(RawModel):
    following: bool
    notification: bool
    follow_date: Optional[Annotated[datetime, AfterValidator(to_kst)]] = None


class PersonalData(RawModel):
    private_user_block: bool
    following: Optional[Following] = None


class SubscriptionPaymentAvailability(RawModel):
    iap_availability: bool
    iab_availability: bool


class PartialChannel(RawModel):
    channel_id: Optional[str] = None
    channel_name: str
    channel_image_url: Optional[str] = None
    verified_mark: bool
    personal_data: Optional[PersonalData] = None
    subscription_availability: Optional[bool] = None
    subscription_payment_availability: Optional[SubscriptionPaymentAvailability] = None


class Channel(PartialChannel):
    channel_type: Optional[str] = None
    channel_description: str
    follower_count: int
    open_live: bool


class LivePollingStatus(RawModel):
    status: str
    is_publishing: bool
    playable_status: str
    traffic_throttling: int
    call_period_millisecond: int = Field(alias="callPeriodMilliSecond")


class LiveStatus(RawModel):
    live_title: str
    status: str
    concurrent_user_count: int
    accumulate_count: int
    paid_promotion: bool
    adult: bool
    chat_channel_id: str
    category_type: Optional[str] = None
    live_category: Optional[str] = None
    live_category_value: str
    live_polling_status: Json[LivePollingStatus] = Field(alias="livePollingStatusJson")
    fault_status: Any
    user_adult_status: Optional[str]
    chat_active: bool
    chat_available_group: str
    chat_available_condition: str
    min_follower_minute: int
    chat_donation_ranking_exposure: bool


class LivePlaybackMetaCDNInfo(RawModel):
    cdn_type: str
    zero_rating: bool


class LivePlaybackMeta(RawModel):
    video_id: str
    stream_seq: int
    live_id: str
    paid_live: bool
    cdn_info: LivePlaybackMetaCDNInfo
    # p2p: bool = Field(alias="p2p")
    cmcd_enabled: bool


class LivePlaybackServiceMeta(RawModel):
    content_type: str


class LivePlaybackLive(RawModel):
    start: Annotated[datetime, AfterValidator(to_kst)]
    open: Annotated[datetime, AfterValidator(to_kst)]
    time_machine: bool
    status: str


class LivePlaybackAPI(RawModel):
    name: str
    path: str


class LivePlaybackVideoTrack(RawModel):
    encoding_track_id: str
    video_profile: str
    audio_profile: str
    video_codec: str
    video_bit_rate: int
    audio_bit_rate: int
    video_frame_rate: float
    video_width: int
    video_height: int
    audio_sampling_rate: int
    audio_channel: int
    avoid_reencoding: bool
    video_dynamic_range: str


class LivePlaybackAudioTrack(RawModel):
    encoding_track_id: str
    path: str
    audio_codec: str
    audio_bit_rate: int
    audio_only: bool
    audio_sampling_rate: int
    audio_channel: int
    avoid_reencoding: bool


class LivePlaybackMedia(RawModel):
    media_id: str
    protocol: str
    path: str
    latency: Optional[str] = None
    encoding_track: list[Union[LivePlaybackVideoTrack, LivePlaybackAudioTrack]]


class LivePlaybackThumbnail(RawModel):
    snapshot_thumbnail_template: str
    time_machine_thumbnail_template: Optional[str] = None
    types: list[str]


class LivePlayback(RawModel):
    meta: LivePlaybackMeta
    service_meta: LivePlaybackServiceMeta
    live: LivePlaybackLive
    api: list[LivePlaybackAPI]
    media: list[LivePlaybackMedia]
    thumbnail: LivePlaybackThumbnail
    multiview: list[Any]


class Live(RawModel):
    live_title: str
    live_image_url: Optional[str]
    default_thumbnail_image_url: Optional[str] = None
    concurrent_user_count: int
    accumulate_count: int
    open_date: Annotated[datetime, AfterValidator(to_kst)]
    live_id: int
    adult: bool
    chat_channel_id: str
    category_type: Optional[str] = None
    live_category: Optional[str] = None
    live_category_value: str
    channel_id: Optional[str] = None
    live_playback: Json[LivePlayback] = Field(alias="livePlaybackJson")


class LiveDetail(Live):
    status: str
    close_date: Optional[Annotated[datetime, AfterValidator(to_kst)]] = None
    chat_active: bool
    chat_available_group: str
    paid_promotion: bool
    chat_available_condition: str
    min_follower_minute: int
    channel: PartialChannel
    live_polling_status: Json[LivePollingStatus] = Field(alias="livePollingStatusJson")
    p2p_quality: list[Any] = Field(alias="p2pQuality")
    user_adult_status: Optional[str]
    chat_donation_ranking_exposure: bool


class VideoMetadata(RawModel):
    video_no: int
    video_id: str
    video_title: str
    video_type: str
    publish_date: Annotated[datetime, AfterValidator(to_kst)]
    thumbnail_image_url: str
    duration: int
    read_count: int
    channel_id: Optional[str] = None
    publish_date_at: Annotated[datetime, AfterValidator(as_kst)]
    adult: bool
    category_type: Optional[str] = None
    video_category: str
    video_category_value: str


class PartialVideo(VideoMetadata):
    trailer_url: Optional[str] = None
    exposure: bool
    video_category: Optional[str]
    channel: PartialChannel


class Video(PartialVideo):
    paid_promotion: bool
    in_key: str
    live_open_date: Annotated[datetime, AfterValidator(to_kst)]
    vod_status: str
    user_adult_status: Optional[str]

    prev_video: Optional[PartialVideo] = None
    next_video: Optional[PartialVideo] = None


class Offset(RawModel):
    offset: int


class Page(RawModel):
    next: Offset


class SearchCursor(RawModel, Generic[T]):
    size: int
    page: Optional[Page] = None
    data: list[T]


class SearchRecord(RawModel):
    pass


class VideoSearchRecord(SearchRecord):
    video: VideoMetadata
    channel: PartialChannel


class LiveSearchRecord(SearchRecord):
    live: Live
    channel: PartialChannel


class ChannelSearchRecord(SearchRecord):
    channel: Channel
