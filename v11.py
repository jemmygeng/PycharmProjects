from urllib import request, error

if __name__ == '__main__':
    url = "http://www.renren.com/965187997/profile"
    rsp = request.urlopen(url)

    html = rsp.read().decode('utf-8')

    with open("rsp.html", "w") as f:
        f.write(html)