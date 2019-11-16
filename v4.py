from urllib import request, parse
import chardet
if __name__ == '__main__':
    url = "https://www.baidu.com/s?"
    wd = input("Input your keyword:")

    # 想要使用data 需要使用字典
    qs = {
        "wd": wd
    }
    # 转换url编码
    qs = parse.urlencode(qs)
    print(qs)
    fullurl = url + qs

    print(fullurl)
    rsp = request.urlopen(fullurl)

    html = rsp.read()

    # 利用chardet自动检测
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)

    # 用get 取值保证不会出错
    html = html.decode(cs.get("encoding", "utf-8"))
    print(html)
