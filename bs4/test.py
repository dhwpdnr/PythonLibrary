import requests
import json
from pprint import pprint

url = "https://m.coupang.com/vm/sdp/v3/mweb/products/6974393264/option-tree-list?itemId=17019560505&vendorItemId=89321486763&expandType=2439"
# https://m.coupang.com/vm/sdp/v3/mweb/products/6974393264/option-tree-list?itemId=17019560505&vendorItemId=89321486763&expandType=11053
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
}
res = requests.get(url, headers=headers)
data = json.loads(res.text)
pprint(data)
