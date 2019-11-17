'''
 访问一个网站
 更改自己的UserAgent进行伪装
'''
from urllib import request, error
if __name__ == '__main__':
    url="http://wwww.baidu.com"

    try:
        # 使用head方法进行伪装url
        # headers = {}
        #headers['User-Agent'] = "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5"


        #req=request.Request(url, headers=headers)
        req = request.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
        # 正常访问
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print("httperror:{0}".format(e))
    except error.URLError as e:
        print(e)
    except error as e:
        print(e)