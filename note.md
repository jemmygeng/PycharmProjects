# 2. urllib
- 包含模块
    - urllib.request: 打开和读取urls
    - urllib.error: 包含urllib.request产生的常见错误，使用try捕捉
    - urllib.parse: 包含解析url的方法
    - urllib.robotparse: 解析robots.txt文件
- 网页编码问题解决
    - chardet 可以自动检测页面文件的编码格式，但是 可能有误
    - 需要安装，conda install chardet
    - 案例v2
- urlopen 返回的对象
    - 案例v3
    - geturl:返回请求对象的url
    - info: 请求反馈对象的meta信息
    - getcode: 返回的http code

- request.data 的使用
    - 访问网络的两种方法
        - get:
            - 利用参数给服务器传递信息
            - 参数为dict,然后用parse编码
            - 案例v4
        - post:
            - 一般向服务器传递参数使用
            - post是把信息自动加密处理
            - 我们如果想使用post信息，需要用到data参数
            - 使用post,意味着HTTP请求头可能需要更改：
                - Content-Type:application/x-www.form-urlencode
                - Content-Length: 数据长度
                - 简而言之 一旦更改请求方法，请注意其他请求头部信息相适应
            - urllib.parse.urlencode可以将字符串自动转换成上面的
            - 案例5
            - 为了更多的设置请求信息，单纯的通过urlopen函数已经不大好用了
            - 需要利用request.Request 类
            - 案例v6
- urllib.error
    - URLError产生的原因：
        - 没网
        - 服务器链接失败
        - 知不道指定服务器
        - 是OSError的子类
        - 案例V7
    - HTTPError, 是URLError的一个子类
        - 案例V8

    - 两者区别：
        - HTTPError是对应的HTTP请求的返回错误，如果返回错误码是400以上的，则引发HTTPError
        - URLError对应的一般是网络出现问题，包括url问题
        - 关系区别： OSError-URLError-HTTPError
- UserAgent
    - UserAgent: 用户代理，简称UA, 属于heads的一部分，服务器通过UA来判断访问者身份
    - 常见的UA值，使用的时候可以直接复制粘贴，也可以用浏览器访问的时候抓包
        1.Android
            Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
            Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
        2.Googole chrome
            Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36
            Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11
            Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16
    - 设置UA可以通过两种方式：
        - heads
        - add_header
        - 案例v9
- ProxyHandler处理（代理服务器）
    - 使用代理IP,是爬虫的常用手段
    - 获取代理服务器的地址：
        - wwww.xicidaili.com
        - wwww.goubanjia.com
    - 代理用来隐藏真实访问，代理也不允许频繁访问某一个固定网站，所以，代理一定要很多很多
    - 基本使用步骤：
        1. 设置代理地址
        2. 创建ProxyHandler
        3. 创建Opener
        4. 安装Opener
    - 案例10
- cookie & session
    - 由于http协议无记忆性，人们为了弥补这个缺憾，所采用的一个补充协议
    - cookie是发放给用户（即http浏览器）的一段信息，session 是保存在服务器上的对应的另一半信息，用来记录用户信息

- cookie和session的区别
    - 存放位置不同
    - cookie不安全
    - session 会保存在服务器上一定时间，会过期
    - 单个cookie保存数据不超过4k,很多浏览器限制一个网站最多保存20个
- session 的存放位置
    - 存在服务器端
    - 一般情况，session是放在内存中或者数据库中
    - 没有cookie登陆 案例v11 可以看到，没有cookie则反馈网
- 使用cookie登陆
    - 直接把cookie 复制下来，然后手动放入请求头，案例V12
    - http模块包含一些关于cookie的模块，通过他们 我们可以自动使用cookie
        - CookieJar
            - 管理存储cookie,向传出的http请求添加cookie,
            - cookie存储在内存中，CookieJar实例回收后cookie将消失
        - FileCookieJar（filename, delayload=None, policy=None）
            - 使用文件管理cookie
            - filename是保存cookie的文件
        - MozillaCookieJar（filename, delayload=None, policy=None）
            - 创建与mocilla浏览器cookie,txt兼容的FileCookieJar实例’
        - LwpCookieJar（filename, delayload=None, policy=None）
            - 创建与libww-perl标准兼容的Set-Cookie3格式的FileCookieJar实例
        - 它们的关系是：CookieJar-->FileCookieJar-->MozillaCookieJar & LwpCookieJar
    - 利用cookieJar访问人人网 案例v13
        - 自动使用cookie登录，大概流程是：
            - 打开登录页面后自动通过用户名密码登录
            - 自动提取反馈回来的cookie
            - 利用提取的cookie登录隐私页面
    - handler是Handler的实例 常用的参考示例代码
       - 用来处理复杂请求
            - 生成cookie的管理器
               cookie_handler = request.HTTPCookieProcessor(cookie)
            -  创建http请求管理器
               http_handler = request.HTTPHandler()
            - 生成https管理器
               https_handler = request.HTTPSHandler()
    - 创建handler后使用opener打开，打开后相应的业务由相应的handler处理
    - cookie作为一个变量，打印出来 案例v14
        - cookie 的属性
            - name: 名称
            - value: 常见的UA值
            - domain: 可以访问此cookie的域名
            - path: 可以访问此cookie的页面路径
            - expires: 过期时间
            - size: 大小
            - Http字段

    - cookie 的保存- FileCookieJar 案例v15
    - cookie 的读取，案例v16
- SSL
    - SSL证书就是指遵守SSL安全套阶层协议的服务器数字证书（SercureSocketLayer）
    - 美国网景公司开发
    - CA(CertifacateAuthority)是数字证书认证中心，是发放，管理，废除数字证书的收信人的第三方机构
    - 遇到不信任的SSL证书，需要单独处理 案例V17
- js加密
    - 有的反爬虫策略采用了js对需要传输的数据进行加密处理（通常是取MD5值）
    - 经过加密，传输的就是密文，但是
    - 加密函数或者过程一定是在浏览器完成，也即是一定会把代码（js代码）暴露给使用者
    - 通过阅读加密算法，就可以模拟出加密过程，从而达到破解
    - 过程参见案例v18 ,v19
- ajax
    - 异步请求
    - 一定会有url，请求方法，可能有数据
    - 一般用json格式
    - 案例，爬取豆瓣电影，案例V20
# Requests- 献给人类
- HTTP for Humans,更简洁 更友好
- 继承了urllib的所有特征
- 底层使用的是urllib3
- 开源地址：https://github.com/request/requests
- 中文文档：http://docs.python-requests.org/zh_CN/lastest/index.html
- 安装：conda install request
- get请求
    - requests.get(url)
    - requests.request("v22get",url)
    - 可以带有headers和parmas参数
    - 案例v21
- get返回内容
    - 案例v22
- post
    - rsp = request.post(url,data=data)
    - 案例23
    - data,headers 要求dict类型







