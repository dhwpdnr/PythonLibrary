import requests
import json
from pprint import pprint
from urllib.parse import urlparse, parse_qs

base_url = "https://www.coupang.com"
url = "https://www.coupang.com/vp/products/6974393264?itemId=17019560507&searchId=be4ffe0af2324a92a3e3bfaf9ec050d6&sourceType=brandstore_sdp_atf-baseline_list&storeId=143296&subSourceType=brandstore_sdp_atf-baseline_list&vendorId=A01026686&vendorItemId=86451248472&isAddedCart="
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
}

parsed_url = urlparse(url)
path_segments = parsed_url.path.split("/")
product_id = path_segments[-1]  # 경로의 마지막 부분이 상품 ID입니다.

# 요청할 URL 구성
url = f"https://www.coupang.com/vm/v4/enhanced-pdp/products/{product_id}"

# GET 요청 실행
response = requests.get(url, headers=headers)
data = json.loads(response.text)
first_options = data["rData"]["product"]["entityList"][2]["entity"]["options"]

print(f"상품명 : {data['rData']['product']['productDto']['name']}")
print("__________________________________")

for option in first_options:
    # print(option["name"])
    # print(option["requestUri"])
    response = requests.get(base_url + option["requestUri"], headers=headers)
    option_data = json.loads(response.text)["rData"]["options"]
    for opt in option_data:
        print(f"옵션명 : {option['name']}, {opt['name']}")
        print(f'가격 {opt["i18nSalesPrice"]["amount"]}원')
        print()
