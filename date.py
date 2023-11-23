import datetime

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

