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
        nid_auth="Your NID_AUT",
        nid_session="Your NID_SES",
    )
    chzzk = Chzzk(credential)

    print(await chzzk.channel("bdc57cc4217173f0e89f63fba2f1c6e5"))
    print(await chzzk.video(1794))


if __name__ == "__main__":
    asyncio.run(main())
```

## Acknowledgement
- Thanks [kimcore/chzzk](https://github.com/kimcore/chzzk) for sharing API urls and explaining how it works.