import pika
from pika import connection
from pika import channel

params = pika.URLParameters("amqps://lrtmtglx:oYHJOduxC6B0WByra-d6Rzw0ge8R8sLY@hornet.rmq.cloudamqp.com/lrtmtglx")
connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue="admin")

def callback(ch,method,properties,body):
    print("Received in admin")
    print(body)

channel.basic_consume(queue="admin",on_message_callback=callback,auto_ack=True)
print("Started consuming")
channel.start_consuming()
channel.close()