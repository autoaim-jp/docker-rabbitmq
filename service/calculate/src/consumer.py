import pika

credentials = pika.PlainCredentials("root", "password")
connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq", port=5672, credentials=credentials))

queue_name = "greet"
channel = connection.channel()
channel.queue_declare(queue=queue_name)

def callback(ch, method, props, body):
    print("Received:", body)
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
print("Waiting for messages ...")
channel.start_consuming()

