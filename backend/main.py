from fastapi import FastAPI, Depends, HTTPException
from database.db import SessionLocal, init_db
from services.note_service import NoteService
from database.models import Note
from sqlalchemy.orm import Session

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Initialize the database on startup
@app.on_event("startup")
def on_startup():
    init_db()

# Create a new note
@app.post("/notes/", response_model=Note)
def create_note(title: str, content: str, tags: str = "", db: Session = Depends(get_db)):
    service = NoteService(db)
    return service.create_note(title, content, tags)

# Get all notes
@app.get("/notes/", response_model=list[Note])
def get_notes(db: Session = Depends(get_db)):
    service = NoteService(db)
    return service.get_all_notes()

# Get a single note by ID
@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int, db: Session = Depends(get_db)):
    service = NoteService(db)
    note = service.get_note(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

# Update a note
@app.put("/notes/{note_id}", response_model=Note)
def update_note(note_id: int, title: str, content: str, tags: str, db: Session = Depends(get_db)):
    service = NoteService(db)
    updated_note = service.update_note(note_id, title, content, tags)
    if not updated_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return updated_note

# Delete a note
@app.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    service = NoteService(db)
    success = service.delete_note(note_id)
    if not success:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note deleted successfully"}