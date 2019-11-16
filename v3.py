from urllib import  request
import chardet
if __name__ == '__main__':
    url = "http://stock.eastmoney.com/a/201911161293836315.html"

    rsp = request.urlopen(url)

    print(rsp)

    print("URL: {0}".format(rsp.geturl()))
    print("Info: {0}".format(rsp.info()))
    print("Code:{0}".format(rsp.getcode()))
    html = rsp.read()

    # 利用chardet自动检测
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)

    # 用get 取值保证不会出错
    html = html.decode(cs.get("encoding", "utf-8"))
    print(html)


