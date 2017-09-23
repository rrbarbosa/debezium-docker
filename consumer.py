import json
from kafka import KafkaConsumer


consumer = KafkaConsumer(bootstrap_servers="kafka",
                         group_id=None,
                         auto_offset_reset='earliest')
consumer.subscribe(['dbserver1.inventory.customers'])
m = next(consumer)
json.loads(m)
json.loads(m.key)
json.loads(m.value)
