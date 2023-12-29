from datetime import datetime, timedelta, timezone

kst = timezone(timedelta(hours=9))


def to_kst(time: datetime) -> datetime:
    return time.replace(tzinfo=kst)


def as_kst(time: datetime) -> datetime:
    return time.astimezone(tz=kst)
