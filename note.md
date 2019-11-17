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



