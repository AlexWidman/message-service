from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

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