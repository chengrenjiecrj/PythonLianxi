import pika
import sys

def sendMQ():
    credentials = pika.PlainCredentials('bt', '123qwe')  # 注意用户名及密码
    connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='10.143.117.32',virtual_host='sit'))
            # host='10.143.117.32',port=5672,virtual_host='/exchanges',credentials=credentials))
    channel = connection.channel()

    channel.exchange_declare(exchange='cache.limit.exchange',
                             type='fanout')

    # message = ' '.join(sys.argv[1:]) or "info: Hello World!"  #如果键盘有输入，message为键盘输入，如果键盘没有输入，消息message="info: Hello World!"；
    message = '{"channelId":"001","limit":"20000","userId":"100039974307","state":"S","createdTime":1516784256320,"id":1601,"customerId":"927fad6e-8f81-4c23-a0f8-5a926a3621b5"}'
    channel.basic_publish(exchange='cache.limit.exchange', routing_key='', body=message)
    print(" [x] Sent %r" % (message,))
    connection.close()

def reviceMQ():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='logs',
                             type='fanout')

    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='logs',
                       queue=queue_name)

    print(' [*] Waiting for logs. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(" [x] %r" % (body,))

    channel.basic_consume(callback,
                          queue=queue_name,
                          no_ack=True)

    channel.start_consuming()

if __name__ == '__main__':
    sendMQ()
    # reviceMQ()