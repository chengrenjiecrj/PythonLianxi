from urllib import parse
url = 'http://10.152.4.78:7080/promotioninformation/querypromotioninformation/{id}'
data = {"id":"27"}
params = "?"
parseResult = parse.urlparse(url)
print(parseResult)

print(url.count("{id}"))
if url.count("{id}") >= 0:
    # urls = urlparse.urlsplit(url)
    # print(urls)
    url = url.replace("{id}",data["id"])
    params = ""
    print("OK  "+url)
print(url+"   "+params)