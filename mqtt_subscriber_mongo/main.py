import paho.mqtt.client as mqtt
import json
from pymongo import MongoClient

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload)
    # Parse and convert the timestamp to a date object
    timestamp = datetime.fromisoformat(payload["timestamp"])
    payload["timestamp"] = timestamp
    # Insert the payload into MongoDB
    db_collection.insert_one(payload)

client = mqtt.Client()
client.connect("mqtt-broker", 1883, 60)
client.subscribe("sensors/temperature")

client.on_message = on_message

# MongoDB setup
mongo_client = MongoClient("mongodb://mongo:27017/")
db = mongo_client["sensor_data"]
db_collection = db["temperature_data"]

client.loop_forever()
