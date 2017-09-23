import json
from kafka import KafkaConsumer


consumer = KafkaConsumer(bootstrap_servers="kafka",
                         group_id=None,
                         auto_offset_reset='earliest')
consumer.subscribe(['dbserver1.inventory.customers'])
m = next(consumer)

print(json.loads(m.key))
print(json.loads(m.value))
