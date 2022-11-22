from kafka import KafkaProducer

bootstrap_server = ["localhost:9092"]

topic = "nestDigi"

producer = KafkaProducer(bootstrap_servers = bootstrap_server)

producer = KafkaProducer()

data = "Hi Hello"

message = producer.send(topic,bytes(data,"utf-8"))

metadata = message.get()
print(metadata.topic)
print(metadata.partition)