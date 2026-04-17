from fastapi import FastAPI
from database import engine, Base, SessionLocal
from sensor_simulator import generate_sensor_data
from models import SensorData
import threading

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Sensor Monitoring System Running"}


@app.get("/sensors")
def get_sensor_data():

    db = SessionLocal()

    data = db.query(SensorData).order_by(
        SensorData.timestamp.desc()
    ).limit(20).all()

    db.close()

    return data


@app.on_event("startup")
def start_sensor():

    thread = threading.Thread(target=generate_sensor_data)

    thread.daemon = True

    thread.start()