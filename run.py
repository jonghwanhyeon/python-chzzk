import asyncio

from chzzk import Chzzk
from chzzk.client import Credential


async def main():
    chzzk = Chzzk(
        Credential(
            nid_auth="w3kvHDBy7+B/rvaPGcvusyp3IvunbtJWQIfZOAX1mSvisgMNBUg6vo320DGmUqSw",
            nid_session="AAABqzuRWjsdfaZDf66Ms4LhTZnbF7spL+AJqDKrZK4KAe/BtW81A/3Dyhi2TXQTh91uRVwpp4HcK5GWOY9ALLA70RDoLZOfetD9TZA0yTHL1Bkj9H+/M5INXHY7IdWgWrNiqa2MFovzrhPmCQc6/i4dbUp8grnYgt+JlWnWTQajxqvkYfnTqbsdnHYRtjCrCGJvkAT15jk/x6kOWQwFo14WHV8noduFR+xHciawMFF4uwnheKiQxTWrUNadVXjivwMp/ofsCKr9C2BNrLmPhuRpJ0O103HKiVn1TlWj95u2sUvWIED2ivpRLR7yAUKaxGzbeWe6n3GuRkL24B43mRWQ9KVKdURIGzbuBNeVkBuXj+OoWEhCWrySD18bVyaiIKcV3o603rh16Mde3ceOFk69Q/ZGiO5GTovbUyUH1B3EOhwbUD3qzV18n3AuoPWEIsSfD/MjCwl8UHA78IbM6l9BdeMETvlkT/rCJsOi7bdENzNPVdSmH+6YrYrZ6g6eJZnZZZ76iIUCAbuzQg5+u3c824lXTi3RbIPlZtYX9RdZmdu/On9TfAILALnuxamlMrRbTA==",
        )
    )

    print(await chzzk.me())
    print(await chzzk.channel("bb382c2c0cc9fa7c86ab3b037fb5799c"))


if __name__ == "__main__":
    asyncio.run(main())
