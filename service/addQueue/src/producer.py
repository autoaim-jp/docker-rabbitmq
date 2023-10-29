import pika


credentials = pika.PlainCredentials("root", "password")
connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq", port=5672, credentials=credentials))

queue_name = "greet"
channel = connection.channel()
channel.queue_declare(queue=queue_name)

message = "hello, world!"
channel.basic_publish(exchange="", routing_key=queue_name, body=message)
print("Sent:", message)

connection.close()

