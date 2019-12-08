from urllib import request, error, parse
# r = "" + (new Date).getTime()   , i = r + parseInt(10 * Math.random(), 10);
# n.md5("fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj")

def getts():
    import time
    ts = int(time.time()*1000)
    return ts
def getsalt(ts):
    import random
    salt = str(ts) + str(random.randint(0, 10))
    return salt

def getMD5(v):
    import hashlib
    md5 = hashlib.md5()
    md5.update(v.encode('utf-8'))
    sign = md5.hexdigest()
    return sign

def getSign(key,salt):
    sign = 'fanyideskweb' + key + str(salt) + "n%A-rKaT5fb[Gy?;N5@Tj"
    sign = getMD5(sign)
    return sign

def getbv():
    bv = getMD5("5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36")
    return bv

def fanyi(key):
    import time
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    xx = getts()
    time.sleep(0.03)
    ts = getts()
    print(xx, ts)

    salt = getsalt(ts)
    sign = getSign(key, salt)
    data = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": str(salt),
        "sign": str(sign),
        "ts": str(ts),
        "bv": str(getbv()),
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME",
    }
    print(data)
    # 参数data需要转为byte格式
    data = parse.urlencode(data).encode()
    header = {
        "Accept": "application/json,text/javascript,*/*;q=0.01",
        #"Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": len(data),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=-1274320560@10.169.0.83;JSESSIONID=aaal5YoMhx_qegcTheY6w;OUTFOX_SEARCH_USER_ID_NCOO=2115691519.8633332; ___rl__test__cookies="+str(ts),
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }

    req = request.Request(url=url, data=data, headers=header)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    print(html)


if __name__ == '__main__':
    key = input("请输入你要查的词\r\n")
    while ( key!=""):
        fanyi(str(key))
        key = input("请输入你要查的词\r\n")
