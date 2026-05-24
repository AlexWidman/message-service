from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlits:///./messages.db"

engine = create_engine(
    DATABASE_URL
)

# Create session for interacting with the database
SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)

# Base for Message class
Base = declarative_base()