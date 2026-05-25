from fastapi import FastAPI

from app.database import engine, Base
from app.models import Message

Base.metadata.create_all(bind = engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Message service is running"}