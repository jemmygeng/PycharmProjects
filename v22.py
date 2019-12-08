'''
使用参数headers和params
研究返回结果
'''
import requests

url = "https://wwww.baidu.com/s?"
kw = {
    "wd": "王八蛋"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
rsp = requests.get(url, params=kw, headers=headers)
print(rsp.text)
print(rsp.content)
print(rsp.url)
print(rsp.encoding)
print(rsp.status_code)