# python-chzzk
An unofficial Python library for CHZZK. **Caution**: APIs are currently experimental.

## Requirements
- Python 3.8+

## Installation
```
pip install python-chzzk
```

> [!NOTE]
> 지금 보고 계시는 fork 버전인 `zer0ken/python-chzzk`을 설치하려면 다음 명령어를 실행하세요.
> ```
> pip install -e git+https://github.com/zer0ken/python-chzzk.git@main#egg=python-chzzk
> ```

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
