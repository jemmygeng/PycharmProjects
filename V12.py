from urllib import request, error

if __name__ == '__main__':
    url = "http://www.renren.com/965187997/profile"
    headers={
        "Cookie": "xxxxxxx"

    }

    req = request.Request(url, headers=headers)

    rsp = request.urlopen(req)
    html = rsp.read().decode()

    with open("rsp.html", "w") as f:
        f.write(html)



