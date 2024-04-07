import requests
import json

url = "https://m.coupang.com/vm/sdp/v3/mweb/products/6974393264/option-tree-list?itemId=17019560505&vendorItemId=89321486763&expandType=11053&selectedItemId=17019560505&selectedVendorItemId=89321486763&sdp-st=H4sIAAAAAAAAAE2OQQqDMBRE7_LXLowxUbMuhUKhQu0BUv3IhzSWmFiK5O5Voba74c08mBlulnztqMVm6HuDtXb6MYKaIdhXB8q7gDGBy9PTYBt9_18YIlCsSFklZCpSkYCZVlRWPGN5KQvJd_WKBts1bPpi782ZRv-FgB4UZDmvYOm3WyfbmtCR7Q9oaEL3PuLvQowfsvaBacEAAAA&metaData=eyJzIjoiTVdFQl9OT1JNQUxfMCIsImsiOiIyNzNmdnQycWk0a2ZtOWEydzciLCJkIjpbeyJ0IjpbMjQzOV0sImUiOjB9LHsidCI6WzExMDUzXSwiZSI6MH1dLCJvIjoxNCwibCI6eyJwIjo2OTc0MzkzMjY0LCJpIjoxNzAxOTU2MDUwNywidiI6ODkxMTY4NTg4OTJ9LCJlIjp7ImUiOmZhbHNlLCJyIjotMSwibmMiOmZhbHNlLCJzZmIiOnRydWUsInNxYiI6dHJ1ZSwic2JzbmIiOmZhbHNlLCJkYnNuYmlkIjoiQ1JNLTY3MDcwX0xvZ291dF93ZWJfMSIsIm5sYyI6ZmFsc2V9fQ"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
}
res = requests.get(url, headers=headers)
if res.status_code == 200:
    data = json.loads(res.text)
    print(data["rData"])
