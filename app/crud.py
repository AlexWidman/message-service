# CREATE, READ, UPDATE, DELETE (CRUD)

from sqlalchemy.orm import Session
from app import models, schemas

# Convert API schema into database model

def create_message(db: Session, message: schemas.MessageCreate):
    db_message = models.Message(
        sender = message.sender,
        recipient = message.recipient,
        content = message.content
    )

    db.add(db_message)      # Prepare for saving in database
    db.commit()             # Commits changes to SQLite
    db.refresh(db_message)  # Reloads object from database, for generated values like id & timestamp

    return db_message


def get_unread_messages(db: Session, recipient: str):
    # Find message based on recipient name
    messages = (
        db.query(models.Message).filter(
            models.Message.recipient == recipient,
            models.Message.is_read == False
        ).all()
    )

    for message in messages:    # Set all unread messages to read
        message.is_read = True

    db.commit()

    return messages


def delete_message(db: Session, message_id: int):
    # Find message based on id
    message = (
        db.query(models.Message).filter(models.Message.id == message_id).first()
    )

    if message is None:     # Returns None if message not found
        return None
    
    db.delete(message)
    db.commit()

    return message