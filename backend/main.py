from fastapi import FastAPI
from db import Base, engine
from models import Job

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Clone Platform Backend Running"}