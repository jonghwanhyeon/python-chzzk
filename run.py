import asyncio

from python_chzzk import Chzzk
from python_chzzk.client import Credential


async def main():
    credential = Credential(
        auth="w3kvHDBy7+B/rvaPGcvusyp3IvunbtJWQIfZOAX1mSvisgMNBUg6vo320DGmUqSw",
        session="AAABqzuRWjsdfaZDf66Ms4LhTZnbF7spL+AJqDKrZK4KAe/BtW81A/3Dyhi2TXQTh91uRVwpp4HcK5GWOY9ALLA70RDoLZOfetD9TZA0yTHL1Bkj9H+/M5INXHY7IdWgWrNiqa2MFovzrhPmCQc6/i4dbUp8grnYgt+JlWnWTQajxqvkYfnTqbsdnHYRtjCrCGJvkAT15jk/x6kOWQwFo14WHV8noduFR+xHciawMFF4uwnheKiQxTWrUNadVXjivwMp/ofsCKr9C2BNrLmPhuRpJ0O103HKiVn1TlWj95u2sUvWIED2ivpRLR7yAUKaxGzbeWe6n3GuRkL24B43mRWQ9KVKdURIGzbuBNeVkBuXj+OoWEhCWrySD18bVyaiIKcV3o603rh16Mde3ceOFk69Q/ZGiO5GTovbUyUH1B3EOhwbUD3qzV18n3AuoPWEIsSfD/MjCwl8UHA78IbM6l9BdeMETvlkT/rCJsOi7bdENzNPVdSmH+6YrYrZ6g6eJZnZZZ76iIUCAbuzQg5+u3c824lXTi3RbIPlZtYX9RdZmdu/On9TfAILALnuxamlMrRbTA==",
    )
    chzzk = Chzzk(credential)

    print('me:')
    print(await chzzk.me())
    print('channel:')
    print(await chzzk.channel("bdc57cc4217173f0e89f63fba2f1c6e5"))
    print('video:')
    print(await chzzk.video(1794))
    print('search channels:')
    print(await chzzk.search.channels("풍월량"))
    print('search videos:')
    print(await chzzk.search.videos("자낳대"))
    print('search lives:')
    print(await chzzk.search.lives("타르코프"))
    print('live status:')
    print(await chzzk.live.status(channel_id="22bd842599735ae19e454983280f611e"))
    print('live detail:')
    print(await chzzk.live.detail(channel_id="22bd842599735ae19e454983280f611e"))


if __name__ == "__main__":
    asyncio.run(main())
