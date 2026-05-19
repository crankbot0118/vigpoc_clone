from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)
from datetime import datetime
from db import Base


class Instance(Base):
    __tablename__ = "instances"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)


class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)

    instance_id = Column(Integer, ForeignKey("instances.id"), unique=True)


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    status = Column(String(50), nullable=False)

    source_instance_id = Column(Integer)
    target_instance_id = Column(Integer)

    created_on = Column(DateTime, default=datetime.utcnow)
    last_update_on = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)