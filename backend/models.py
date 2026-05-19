from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base

class Instance(Base):
    __tablename__ = "instances"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    # One Instance -> Many Jobs
    jobs = relationship(
        "Job",
        back_populates="target_instance"
    )
    # One Instance -> One Agent
    agent = relationship(
        "Agent",
        back_populates="instance",
        uselist=False
    )


class Agent(Base):
    __tablename__ = "agents"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    instance_id = Column(
        Integer,
        ForeignKey("instances.id"),
        unique=True
    )
    # Agent belongs to one Instance
    instance = relationship(
        "Instance",
        back_populates="agent"
    )

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    status = Column(String(50), nullable=False)
    target_instance_id = Column(
        Integer,
        ForeignKey("instances.id")
    )
    created_on = Column(
        DateTime,
        default=datetime.utcnow
    )
    last_update_on = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    # Job belongs to one Instance
    target_instance = relationship(
        "Instance",
        back_populates="jobs"
    )