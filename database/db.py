from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

# SQLite database URL
DATABASE_URL = "sqlite:///./smartnote.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Initialize the database (create tables)
def init_db():
    Base.metadata.create_all(bind=engine)   