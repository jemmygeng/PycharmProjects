from urllib import request
'''
使用urllib。request请求一个网页，并且把内容打印出来
'''
if __name__ == '__main__':
    url = "http://jobs.zhaopin.com/CC444965518J00189517908.htm"
    # 打开相应url并把相应页面作为返回
    rsp = request.urlopen(url)

    # 把返回结果读取出来
    # 读取出来的内容类型为bytes
    html = rsp.read()

    # 如果想把byte内容转换成字符 需要解码
    html = html.decode()
    print(html)
