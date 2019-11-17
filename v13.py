from urllib import request, error, parse
from http import cookiejar

# 新建cookiejar的实例
cookie = cookiejar.CookieJar()
# 生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()

# 生成https管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)

def login():
    '''
    负责初次登录
    需要输入用户名，密码 用来获取登录cookie凭证
    :return:
    '''
    # 此url需要从登录form的action属性中提取
    url = "http://www.renren.com/PLogin.do"
    # 此简直需要从登录form的两个对应的input中提取name属性
    data = {
        "email": "139191144223",
        "password": "123456"
    }

    # 把数据进行编码
    data = parse.urlencode(data)
    # 创建一个请求对象
    req = request.Request(url, data=data.encode())

    # 使用opener 发起请求
    rsp = opener.open(req)

def getHomePage():
    url = "http://www.renren.com/965187997/profile"
    # 如果已经执行了login函数，则opener自动已经包含了相应的cookie
    rsp = opener.open(url)
    html = rsp.read().decode()
    with open("rsp1.html", "w") as f:
        f.write(html)


if __name__ == "__main__":
    login()
    getHomePage()