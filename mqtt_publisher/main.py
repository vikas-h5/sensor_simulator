import paho.mqtt.client as mqtt
import json
import time
import random

def on_publish(client, userdata, mid):
    print("Message Published")

client = mqtt.Client()
client.connect("mqtt-broker", 1883, 60)

while True:
    sensor_id = "sensor_1"
    value = random.uniform(0, 100)
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%S")

    payload = {
        "sensor_id": sensor_id,
        "value": value,
        "timestamp": timestamp
    }

    client.on_publish = on_publish
    client.publish("sensors/temperature", json.dumps(payload), qos=1)
    
    time.sleep(5)  # Publish every 5 seconds
