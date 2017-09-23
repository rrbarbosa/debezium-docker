import json
from flask import Flask, jsonify
from kafka import KafkaConsumer

consumer = KafkaConsumer(bootstrap_servers="kafka",
                         group_id=None,
                         consumer_timeout_ms=500,
                         auto_offset_reset='earliest')
consumer.subscribe(['dbserver1.inventory.customers'])

app = Flask(__name__)


@app.route("/")
def hello():
    data = []
    for m in consumer:
        data.append({"key": json.loads(m.key),
                     "value": json.loads(m.value)})
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
