import json
from pprint import pprint

# templates.json 파일을 읽어서 딕셔너리로 변환
with open("templates.json", "r") as file:
    templates = json.load(file)

# 딕셔너리 출력
template_list = templates["list"]
for template in template_list:
    pprint(template)
    print()
