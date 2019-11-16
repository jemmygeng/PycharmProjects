'''
利用request下载页面
自动检测页面编码
'''
from urllib import  request
import chardet
if __name__ == '__main__':
    url = "https://coding.net/products/repo?utm_source=baidu&utm_medium=cpc&utm_term=gitshiyong&e_creative=33784858015&e_keywordid=149505319196&e_keywordid2=149505319196"

    rsp = request.urlopen(url)

    html = rsp.read()

    # 利用chardet自动检测
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)

    # 用get 取值保证不会出错
    html = html.decode(cs.get("encoding", "utf-8"))
    print(html)


