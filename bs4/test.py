import requests
import json
from pprint import pprint

url = "https://m.coupang.com/vm/sdp/v3/mweb/products/6974393264/option-tree-list?itemId=17019560505&vendorItemId=89321486763&expandType=2439"
# https://m.coupang.com/vm/sdp/v3/mweb/products/6974393264/option-tree-list?itemId=17019560505&vendorItemId=89321486763&expandType=11053
"""https://m.coupang.com/vm/sdp/v3/mweb/products/6974393264
/option-tree-list
?itemId=17019560505
&vendorItemId=89442974404
&expandType=2439
"""

"""
https://m.coupang.com/vm/products/6974393264
?itemId=17019560505
&q=%EC%BF%A0%EB%A1%9C%EB%AF%B8
&sourceType=search
&searchId=50514f3c41794ed2a363e86ab39c3c1a
&filterKey=&wTrackId=50370479998244025147348_1712624132695
&wEntrySource=srp_product_click
&uriScheme=uriScheme
"""

"""
https://www.coupang.com/vp/products/6974393264
?itemId=17019560507
&searchId=be4ffe0af2324a92a3e3bfaf9ec050d6&sourceType=brandstore_sdp_atf-baseline_list
&storeId=143296
&subSourceType=brandstore_sdp_atf-baseline_list
&vendorId=A01026686
&vendorItemId=86451248472
&isAddedCart=
"""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
}
res = requests.get(url, headers=headers)
data = json.loads(res.text)
pprint(data)
