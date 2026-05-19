from fastapi import FastAPI, Depends
from db import Base, engine, SessionLocal
from sqlalchemy.orm import Session
from models import Job

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Clone Platform Backend Running"}

@app.post("/submit-job")
def submit_job(payload: dict, db: Session = Depends(get_db)):

    new_job = Job(
        name=payload["name"],
        status="PENDING",
        source_instance_id=int(payload["source_instance_id"]),
        target_instance_id=int(payload["target_instance_id"])
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return {
        "message": "Job submitted successfully",
        "job_id": new_job.id,
        "status": new_job.status
    }