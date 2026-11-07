from datetime import datetime, timezone, timedelta

iran = timezone(timedelta(hours=3, minutes=30))

date = datetime(2026, 11, 6, 17, 33, 39, tzinfo=iran)

print(int(date.timestamp()))