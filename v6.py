"""
 任务要求和V5一样

 利用parse模块模拟post请求
 分析百度翻译
 分析步骤：
 1.打开F12
 2. 尝试输入单词girl, 发现每敲一个子母后都有请求
 3. 请求地址 https://fanyi.baidu.com/sug
 4. 利用NetWork-All-Headers 查看 发现FormData的值史kw:girl
"""

from urllib import  request, parse
# 负责处理JSON格式的模块
import json

baseurl = 'https://fanyi.baidu.com/sug'

data = {

    'kw': 'girl'
}

# urlencode 进行url编码，encode 编码为字节流
data = parse.urlencode(data).encode('utf-8')

# 需要构造一个请求头，请求头应该至少包含传入的数据的长度
# request 要求传入的请求头是一个dict格式

headers = {
    'Content-Length': len(data)
}


# 构造一个Request实例
req = request.Request(url=baseurl, data=data, headers=headers)

# 因为已经构造了一个Request的请求实例，则所有的请求信息都可以封装在Request实例中
rsp = request.urlopen(req)

json_data = rsp.read().decode('utf-8')
print(type(json_data))
print(json_data)

# 把JSON 字符串转化成字典
json_data = json.loads(json_data)
print(type(json_data))
print(json_data)

for item in json_data['data']:
    print(item['k'], "----", item['v'])