import requests
import json
from pprint import pprint

url = "https://m.coupang.com/vm/sdp/v3/mweb/products/6974393264/option-tree-list?itemId=17019560507&vendorItemId=86451248472&expandType=143296"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
}
res = requests.get(url, headers=headers)

if res.status_code == 200:
    data = json.loads(res.text)
    option_list = data["rData"]["pageList"][0]["widgetList"][0]["data"]["values"]
    type_id = data["rData"]["pageList"][0]["widgetList"][0]["data"]["typeId"]
    option_values = data["rData"]["pageList"][0]["widgetList"][0]["data"]["values"]

    for option in option_values:
        print(f"Item ID: {option['itemId']}")
        print(f"Vendor Item ID: {option['vendorItemId']}")
        print(f"Value Name: {option['valueName']}")
        print(f"Image URL: {option['image']}")
        if "selected" in option:
            print(f"Selected: {option['selected']}")
        print(f"Action URL: {option['action']['event']['url']}\n")
        # item_id = option["itemId"]
        # option_name = option["valueName"]
        # image_url = option["image"]
        # vendor_item_id = option["vendorItemId"]
        # pprint(option)
        # res = requests.get(
        #     f'https://m.coupang.com/vm/sdp/v3/mweb/products/6974393264/option-tree-list?itemId={item_id}&vendorItemId={vendor_item_id}&expandType={type_id}',
        #     headers=headers)
        # print(res.status_code)
        # data = json.loads(res.text)
        # sub_list = data["rData"]["pageList"][0]["widgetList"][0]["data"]["values"]
        # for sub in sub_list:
        #     print(f"아이디 : {sub['itemId']}")
        #     print(f"옵션명 : {sub['itemTitle']}")
        #     print(f"이미지 : {sub['image']}")
        #     print()
        print("__________________________")
