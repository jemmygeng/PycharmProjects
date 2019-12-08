'''
 利用parse模块模拟post请求
 分析百度翻译
 分析步骤：
 1.打开F12
 2. 尝试输入单词girl, 发现每敲一个子母后都有请求
 3. 请求地址 https://fanyi.baidu.com/sug
 4. 利用NetWork-All-Headers 查看 发现FormData的值史kw:girl
'''

import requests
# 负责处理JSON格式的模块
import json
from urllib import parse

baseurl = 'https://fanyi.baidu.com/sug'

data = {

    'kw': 'girl'
}

# urlencode 进行url编码，encode 编码为字节流
# data = parse.urlencode(data).encode('utf-8')

#print(type(data))
# 需要构造一个请求头，请求头应该至少包含传入的数据的长度
# request 要求传入的请求头是一个dict格式

headers = {
    'Content-Length': str(len(data))
}

# 有了headers,data,url 就可以尝试发出请求了

rsp = requests.post(baseurl, data=data,headers= headers)

print(rsp.text)
print(rsp.json())
