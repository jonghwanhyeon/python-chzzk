import asyncio

from chzzk import Chzzk, Credential


NID_AUTH = "<YOUR-NID_AUTH>"
NID_SES = "<YOUR-NID_SES"


async def main():
    credential = Credential(
        auth=NID_AUTH,
        session=NID_SES,
    )
    chzzk_client = Chzzk(credential)

    print("=== Me")
    print(await chzzk_client.me())
    print()

    print("=== Channel")
    print(await chzzk_client.channel("430e71940e6d51309fa6a47fe01e3b30"))
    print()

    print("=== Video")
    print(await chzzk_client.video(1794))
    print()

    print("=== Searched Channels")
    print(await chzzk_client.search.channels("농관전"))
    print()

    print("=== Searched Videos")
    print(await chzzk_client.search.videos("LCK", size=1))
    print()

    print("=== Searched Lives")
    print(await chzzk_client.search.lives("LCK", size=1))
    print()

    print("=== Live Status")
    print(await chzzk_client.live.status(channel_id="430e71940e6d51309fa6a47fe01e3b30"))
    print()

    print("=== Live Detail")
    print(await chzzk_client.live.detail(channel_id="430e71940e6d51309fa6a47fe01e3b30"))


if __name__ == "__main__":
    asyncio.run(main())
