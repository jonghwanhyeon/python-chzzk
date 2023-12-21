from typing import Optional

from chzzk.client import ChzzkClient, Credential, GameClient
from chzzk.models import Channel, User, Video
from chzzk.models import raw as r


class Chzzk:
    def __init__(self, credential: Optional[Credential] = None):
        self._client = ChzzkClient(credential)
        self._game = Game(credential)

    async def me(self) -> User:
        return await self._game.me()

    async def channel(self, id: str) -> Channel:
        response = await self._client.get(f"service/v1/channels/{id}")
        return r.Channel(**response).wrap()

    async def video(self, no: int) -> Video:
        response = await self._client.get(f"service/v1/videos/{no}")
        return r.Video(**response).wrap()


class Game:
    def __init__(self, credential: Optional[Credential] = None):
        self._client = GameClient(credential)

    async def me(self) -> User:
        response = await self._client.get("v1/user/getUserStatus")
        return r.User(**response).wrap()
