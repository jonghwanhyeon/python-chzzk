# python-chzzk
An unofficial Python library for CHZZK. **Caution**: APIs are currently experimental.

## Requirements
- Python 3.8+

## Installation
```python
pip install chzzk
```

## Usage
```python
import asyncio

from chzzk import Chzzk, Credential


async def main():
    credential = Credential(
        auth="Your NID_AUT",
        session="Your NID_SES",
    )
    chzzk = Chzzk(credential)

    print(await chzzk.me())
    print(await chzzk.channel("bdc57cc4217173f0e89f63fba2f1c6e5"))
    print(await chzzk.video(1794))
    print(await chzzk.search.channels("풍월량"))
    print(await chzzk.search.videos("자낳대"))
    print(await chzzk.search.lives("타르코프"))
    print(await chzzk.live.status(channel_id="22bd842599735ae19e454983280f611e"))
    print(await chzzk.live.detail(channel_id="22bd842599735ae19e454983280f611e"))


if __name__ == "__main__":
    asyncio.run(main())
```

## Acknowledgement
- Thanks [kimcore/chzzk](https://github.com/kimcore/chzzk) for sharing API urls and explaining how it works.