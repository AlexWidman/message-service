from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import engine, Base, SessionLocal
from app.models import Message
from app import schemas, crud

Base.metadata.create_all(bind = engine)

app = FastAPI()

# Create database session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Message service is running"}

@app.post("/messages", response_model = schemas.MessageResponse)
def create_message(
    message: schemas.MessageCreate,
    db: Session = Depends(get_db)
):
    return crud.create_message(db, message)

@app.get("/messages/unread/{recipient}", response_model = list[schemas.MessageResponse])
def get_unread_messages(
    recipient: str,
    db: Session = Depends(get_db)
):
    return crud.get_unread_messages(db, recipient)

@app.delete("/messages/{message_id}", response_model = schemas.MessageResponse)
def delete_message(
    message_id: int,
    db: Session = Depends(get_db)
):
    message = crud.delete_message(db, message_id)

    if message is None:
        return {"error": "Message not found"}
    
    return message

@app.delete("/messages", response_model = list[schemas.MessageResponse])
def delete_multiple_messages(
    message_ids: List[int],
    db: Session = Depends(get_db)
):
    return crud.delete_multiple_messages(db, message_ids)

@app.get("/messages", response_model = list[schemas.MessageResponse])
def get_all_messages(
    start: int = 0,
    stop: int | None = None,
    db: Session = Depends(get_db)
):
    return crud.get_all_messages(db, start, stop)

@app.get("/messages/{recipient}", response_model = list[schemas.MessageResponse])
def get_messages(
    recipient: str,
    start: int = 0,
    stop: int | None = None,
    db: Session = Depends(get_db)
):
    return crud.get_messages(db, recipient, start, stop)