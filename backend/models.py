from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker  

Base = declarative_base()  

class Note(Base):  
    __tablename__ = "notes"  
    id = Column(Integer, primary_key=True)  
    evernote_id = Column(String, unique=True)  
    title = Column(String)  
    content = Column(String)  
    tags = Column(String)
    created_at = Column(DateTime)  

class NoteRelationship(Base):  
    __tablename__ = "relationships"  
    id = Column(Integer, primary_key=True)  
    note_id = Column(Integer)  
    related_note_id = Column(Integer)  
    similarity_score = Column(Float)  

 
engine = create_engine("sqlite:///smartnote.db")  
Base.metadata.create_all(engine)  
Session = sessionmaker(bind=engine)  