from urllib import request
from urllib import parse

urlGet = "http://10.152.4.78:7080/getCsrfToken"
dataGet = {}
headersGet = {
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

req = request.Request(urlGet)  # GET方法
page1 = request.urlopen(req).read()
page1 = page1.decode('utf-8')
print(page1)
cstftoken = data["cstftoken"]
token = cstftoken[1]
print(cstftoken)

url = 'http://10.152.4.78:7080/promotioninformation/addorupdatepromotioninformation'
data = {
  "marked_words": "乐享优惠！",
  "promotions": "促销活动S",
  "promotions_num": "20180228190023",
  "state":"1",
  "status": "0",
  "type":"1",
  "id":"27",
  "updated": "20180302140023"
}

params = "?"
# for key in data:
#     if url.count("{"+key+"}") >= 0:
#         url = url.replace("{"+key+"}", data[key])
#         params = ""
#     else:
#         params = params + key + "=" + data[key] + "&"
# print("Get方法参数：" + params)

headers = {
    # heard部分直接通过chrome部分request header部分
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Referer': 'http://10.152.4.78/',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36'
    # 'X-CSRF-TOKEN': page1["token"],
}

data = parse.urlencode(data).encode('utf-8')
req = request.Request(url, headers=headers, data=data)  # POST方法
print("request  "+url)
print(headers)
# req = request.Request(url+params)  # GET方法
page = request.urlopen(req).read()
page = page.decode('utf-8')

print(page)
