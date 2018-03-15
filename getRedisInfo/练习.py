def lianxi1():
    s = 'ilovepython on'
    # 字符串截取
    print(s[4])
    print(s[-3])
    print(s[5:8])

    print(s)
    #用正则表达式替换字符串
    import re
    a = 'hello word'
    strinfo = re.compile('word')
    b = strinfo.sub('python',a)
    print(b)

def datetime():
    import datetime
    nows = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nowdate = datetime.datetime.now().strftime("%Y%m%d")
    date = datetime.datetime.now().date()
    return nowdate

def redis_delete():
    import redis
    pool = redis.ConnectionPool(host='10.143.117.17', port=6379, password='GomeFinance', db=0)
    r = redis.StrictRedis(connection_pool=pool)
    keys = r.keys('*20180223facePay927fad6e-8f81-4c23-a0f8-5a926a3621b5')
    print(type(keys))
    print(keys)
    key = keys[0]
    value = r.get(key)
    print(value)
    print(type(value))
    value = b'okoikeoi2343'
    s2 = bytes.decode(value)
    s3 = value.decode()
    print(s2)
    print(s3)

# 将字节对象decode将获得一个str对象
def bytesToString(bys):
    s2 = bytes.decode(bys)
    s3 = bys.decode()
    # print(s2)
    # print(s3)
    return s3

# 将字符串转换为字节对象
def strToBytes():
    # 字节对象b
    b = b"example"
    # 字符串对象s
    s = "example"
    print(b)
    print("example")
    b2 = bytes(s, encoding='utf8')  # 必须制定编码格式
    # print(b2)
    # 字符串encode将获得一个bytes对象
    b3 = str.encode(s)
    b4 = s.encode()
    print(b3)
    print(type(b3))
    print(b4)

if __name__ == '__main__':
    bytess = b'oieowiewoe'
    st = bytesToString(bytess)
    print(st)