import datetime
import pytz
from pytz import utc, timezone

now = datetime.datetime.now()
print(f"now : {now}")
print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)

print(f"now.weekday() : {now.weekday()}")  # {0:월, 1:화, 2:수, 3:목, 4:금, 5:토, 6:일}
week = {0: "월", 1: "화", 2: "수", 3: "목", 4: "금", 5: "토", 6: "일"}
print(f"{week[now.weekday()]}요일")

day_100_after = now + datetime.timedelta(days=100)
print(f"100일 후 날짜 : {day_100_after}")
day_100_before = now - datetime.timedelta(days=100)
print(f"100일 전 날짜 : {day_100_before}")

# 한국 시간대
KST = datetime.timezone(datetime.timedelta(hours=9))  # UTC+9
korea_1_1 = datetime.datetime(2019, 1, 1, 0, 0, 0, tzinfo=KST)
print(f"한국 시간대 KST(UTC+9) : {korea_1_1}")

# 대만 시간대
TW = datetime.timezone(datetime.timedelta(hours=8))  # UTC+8
taipei_1_1 = datetime.datetime(2019, 1, 1, 0, 0, 0, tzinfo=TW)
print(f"대만 시간대 TW(UTC+8) : {taipei_1_1}")

assert korea_1_1 != taipei_1_1
print("한국 시간대와 대만 시간대는 다릅니다.")
assert taipei_1_1 - korea_1_1 == datetime.timedelta(
    hours=1
)  # 같은 시각이지만 시간대에 따라서 시간차가 있습니다.
print("한국 시간대와 대만 시간대는 1시간 차이가 있습니다.")

naive_1_1 = datetime.datetime(2019, 1, 1, 0, 0, 0)
print(f"datetime.datetime(2019, 1, 1, 0, 0, 0) = {naive_1_1}")

assert korea_1_1 != naive_1_1
print("한국 시간대와 naive 시간대는 다릅니다.")
assert taipei_1_1 != naive_1_1
print("대만 시간대와 naive 시간대는 다릅니다.")

# UTC 시간대 식별자
print("pytz 에서 제공하는 시간대 식별자")
for tz in pytz.all_timezones:
    print(tz)

# UTC 기준 naive datetime : datetime.datetime(2019, 2, 15, 4, 54, 29, 281594)
utc_naive = datetime.datetime.utcnow()
print(f"datetime.datetime.utcnow()은 utc 기준 naive datetime : {utc_naive}")

# 실행 환경 시간대 기준 naive datetime : datetime.datetime(2019, 2, 15, 13, 54, 32, 939155)
local_naive = datetime.datetime.now()
print(f"datetime.datetime.now()은 실행 환경 시간대 기준 naive datetime : {local_naive}")

# UTC 기준 aware datetime : datetime.datetime(2019, 2, 15, 4, 55, 3, 310474, tzinfo=<UTC>)
utc.localize(datetime.datetime.utcnow())
print(
    f"datetime.datetime.utcnow()은 utc 기준 aware datetime : {utc.localize(datetime.datetime.utcnow())}"
)
print("datetime.datetime.utcnow()은 utc 기준 aware datetime이므로, 시간대 변환 없이 사용 가능합니다.")

now = datetime.datetime.utcnow()
print(f"UTC를 기준으로 현재 시각을 생성합니다. 하지만, naive한 시각입니다. : {now}")

assert now != utc.localize(now)

KST = timezone("Asia/Seoul")
TW = timezone("Asia/Taipei")

now = datetime.datetime.utcnow()
print(f"UTC 기준 naive datetime : {now}")

utc.localize(now)
print(f"UTC 기준 aware datetime : {utc.localize(now)}")

KST.localize(now)
print(f"KST 기준 aware datetime : {KST.localize(now)}")

utc.localize(now).astimezone(KST)
print(f"KST 기준 aware datetime : {utc.localize(now).astimezone(KST)}")

date = datetime.datetime.now()

date.replace(hour=10)
print(f"date.replace(hour=10) : {date}")

date.replace(tzinfo=KST)  # tzinfo만 변경
print(f"date.replace(tzinfo=KST) : {date.replace(tzinfo=KST)}")

date.replace(tzinfo=TW)  # tzinfo만 변경
print(f"date.replace(tzinfo=TW) : {date.replace(tzinfo=TW)}")
