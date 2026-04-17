from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database import Base


class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    sensor_name = Column(String, index=True)
    sensor_value = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)