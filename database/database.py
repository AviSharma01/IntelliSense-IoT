from sqlalchemy.orm import Session
from database.models import Base
from database.config import engine

def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()
