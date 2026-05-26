from sqlalchemy import Column, Integer, String, Boolean, DateTime
import datetime as dt

from app.database import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key = True, index = True)
    sender = Column(String, nullable = False)
    recipient = Column(String, nullable = False)
    content = Column(String, nullable = False)

    timestamp = Column(DateTime, default = dt.datetime.now(dt.UTC)) # UTC for simplicity

    is_read = Column(Boolean, default = False)