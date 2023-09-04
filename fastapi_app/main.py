from fastapi import FastAPI
from pymongo import MongoClient
import redis
import json
from datetime import datetime

app = FastAPI()

# MongoDB setup
mongo_client = MongoClient("mongodb://mongo:27017/")
db = mongo_client["sensor_data"]
db_collection = db["temperature_data"]

# Redis setup
redis_client = redis.Redis(host="redis", port=6379, db=0)

@app.get("/sensor-readings")
async def get_sensor_readings(start: str, end: str):
    start_time = datetime.strptime(start, "%Y-%m-%dT%H:%M:%S")
    end_time = datetime.strptime(end, "%Y-%m-%dT%H:%M:%S")
    
    readings = db_collection.find({
        "timestamp": {"$gte": start_time, "$lte": end_time}
    },{"_id":False})
    
    return list(readings)

@app.get("/latest-readings/{sensor_id}")
async def get_latest_readings(sensor_id: str):
    readings = redis_client.lrange(sensor_id, 0, -1)
    return [json.loads(reading) for reading in readings]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
