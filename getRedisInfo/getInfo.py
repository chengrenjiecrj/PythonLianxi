import datetime
def active_redis_get(data):
    import redis
    j_r = redis.Redis(host='10.153.26.63',port=6379,password='123!@#',db=0)
    # key = 'tfms:query:#{cust}#9101###com.bosent.facility.function.facilityQuery.FacilityQueryGome'.format(cust=data)
    nowdate = datetime.datetime.now().strftime("%Y%m%d")
    keys = j_r.keys('*' + nowdate + 'FACEKEY_{custId}'.format(custId=data))
    if keys:
        key = keys[0]
        # print("active: " + bytes.decode(key))
        res = j_r.get(key)
        return res
    else:
        return '没有查到激活face++的redis信息'

def active_redis_delete(data):
    import redis
    j_r = redis.Redis(host='10.153.26.63',port=6379,password='123!@#',db=0)
    # key = 'tfms:query:#{cust}#9101###com.bosent.facility.function.facilityQuery.FacilityQueryGome'.format(cust=data)
    nowdate = datetime.datetime.now().strftime("%Y%m%d")
    keys = j_r.keys('*' + nowdate + 'FACEKEY_{custId}'.format(custId=data))
    if keys:
        key = keys[0]
        # print("active: " + bytes.decode(key))
        res = j_r.delete(key)
        return res
    else:
        return '没有激活face++的redis信息，不用删除'

def gatway_redis_get(data):
    import redis
    g_r = redis.Redis(host='10.143.117.17',port=6379,password='GomeFinance',db=0)
    # key = 'tfms:query:#{cust}#9101###com.bosent.facility.function.facilityQuery.FacilityQueryGome'.format(cust=data)
    # pool = redis.ConnectionPool(host='10.143.117.17', port=6379, password='GomeFinance', db=0)
    # r = redis.StrictRedis(connection_pool=pool)
    # key = '20180223facePay927fad6e-8f81-4c23-a0f8-5a926a3621b5';
    nowdate = datetime.datetime.now().strftime("%Y%m%d")
    keys = g_r.keys('*'+nowdate+'facePay{custId}'.format(custId=data))
    # print(len(keys))
    if len(keys):#keys:
        key = keys[0]
        print(type(key))
        print(key)
        res = g_r.get(key)
        return res
    else:
        return '没有查到支付face++的redis信息'

def gateway_redis_delete(data):
    import redis
    g_r = redis.Redis(host='10.143.117.17', port=6379, password='GomeFinance', db=0)
    nowdate = datetime.datetime.now().strftime("%Y%m%d")
    keys = g_r.keys('*' + nowdate + 'facePay{custId}'.format(custId=data))
    if len(keys):#keys:
        key = keys[0]
        # print("gatway: " + key.decode())
        res = g_r.delete(key)
        return res
    else:
        return '没有支付face++的redis信息，不用删除'

'''def order_redis_get(data):
    import redis
    g_r = redis.Redis(host='10.143.117.17',port=6379,password='GomeFinance',db=0)
    # key = 'tfms:query:#{cust}#9101###com.bosent.facility.function.facilityQuery.FacilityQueryGome'.format(cust=data)
    nowdate = datetime.datetime.now().strftime("%Y%m%d")
    keys = g_r.keys('*' + nowdate + 'facePay{custId}'.format(custId=data))
    key = keys[0]
    res = g_r.delete(key)
    return res
    '''

if __name__ == '__main__':
    # cust = '20180223facePay927fad6e-8f81-4c23-a0f8-5a926a3621b5'
    # cust = '20180223FACEKEY_5449b971-d951-4a71-8105-9ab39c4efc91'

    #支付时候的face++次数
    cust = '927fad6e-8f81-4c23-a0f8-5a926a3621b5'
    a = gatway_redis_get(cust)
    print(a)
    # b = gateway_redis_delete(cust)
    # print(b)
    # c = gatway_redis_get(cust)
    # print(c)

    # 激活时候的face + +次数
    cust = '5449b971-d951-4a71-8105-9ab39c4efc91'
    a = active_redis_get(cust)
    print(a)
    # b = active_redis_delete(cust)
    # print(b)
    # c = active_redis_get(cust)
    # print(c)




    # r.delete("del1", "del2")