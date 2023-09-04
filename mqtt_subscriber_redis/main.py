import paho.mqtt.client as mqtt
import json
import redis

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload)
    # Save payload to Redis
    redis_client.lpush(payload["sensor_id"], json.dumps(payload))
    # Keep only the latest ten readings
    redis_client.ltrim(payload["sensor_id"], 0, 9)

client = mqtt.Client()
client.connect("mqtt-broker", 1883, 60)
client.subscribe("sensors/temperature")

client.on_message = on_message

# Redis setup
redis_client = redis.Redis(host="redis", port=6379, db=0)

client.loop_forever()
