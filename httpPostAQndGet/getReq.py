# import httplib
#
# url = "http://192.168.81.16/cgi-bin/python_test/test.py?ServiceCode=aaaa"
#
# conn = httplib.HTTPConnection("192.168.81.16")
# conn.request(method="GET",url=url)
#
# response = conn.getresponse()
# res= response.read()
# print(res)


# import urllib
# import urllib2
#
# url = "http://192.168.81.16/cgi-bin/python_test/test.py?ServiceCode=aaaa"
#
# req = urllib2.Request(url)
# print(req)
#
# res_data = urllib2.urlopen(req)
# res = res_data.read()
# print(res)
from urllib import request
from urllib import parse

# url = "http://10.152.4.78:7080/getCsrfToken"
# data = {}
# url = 'http://10.152.4.78:7080/promotioninformation/querypromotioninformationlist'
# data = {"pageNum":"1","pageSize":"10"}
url = 'http://10.152.4.78:7080/promotioninformation/querypromotioninformation/{id}'
data = {"id":"27"}

params = "?"
for key in data:
    if url.count("{"+key+"}") >= 0:
        url = url.replace("{"+key+"}", data[key])
        params = ""
    else:
        params = params + key + "=" + data[key] + "&"
print("Get方法参数：" + params)

headers = {
    # heard部分直接通过chrome部分request header部分
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '14',  # get方式提交的数据长度，如果是post方式，转成get方式：【id=wdb&pwd=wdb】
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://10.152.4.78/',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36'
}

data = parse.urlencode(data).encode('utf-8')
# req = request.Request(url, headers=headers, data=data)  # POST方法
print("request  "+url+params)
req = request.Request(url+params)  # GET方法
page = request.urlopen(req).read()
page = page.decode('utf-8')

print(page)

