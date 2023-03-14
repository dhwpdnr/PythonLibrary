import textwrap

text = "Life is too short, you need python. "
long_text = text * 10

print(textwrap.shorten(text, width=15))
print(textwrap.shorten(text, width=15, placeholder="..."))
print(long_text)
result = textwrap.wrap(long_text, width=70)
print(result)
print("\n".join(result))
result_fill = textwrap.fill(long_text, width=70)
print(result_fill)
print()

import re

data = """
주민번호가 텍스트 안에 있을 때
주민번호를 그대로 노출 시키면 안된다
ㅇㅇㅇ 800905-1049118 이나 700950-3244578
이런식으로 있을 때.
데이터를 바꿔줘야 함
"""
print(f"원래 데이터{data}")

# 정규표현식을 사용하지 않고 문자열을 검사해서 바꾸는 방법
line_result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    line_result.append("".join(word_result))
print("\n".join(line_result))

# 정규 표현식을 사용하여 간단하게
pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))
