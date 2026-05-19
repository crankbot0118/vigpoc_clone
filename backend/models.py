from sqlalchemy import Column, Integer, String
from db import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    status = Column(String(50))