from pydantic import BaseModel
from datetime import datetime

# Sending messages without internally generated variables
class MessageCreate(BaseModel):
    sender: str
    recipient: str
    content: str

# Retrieve with internally generated variables
class MessageResponse(BaseModel):
    id: int
    sender: str
    recipient: str
    content: str
    timestamp: datetime
    is_read: bool

    # Read incoming data from different objects and class instances rather than trying to treat as dictionary
    class Config:
        from_attributes = True