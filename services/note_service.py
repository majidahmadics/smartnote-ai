from sqlalchemy.orm import Session
from database.models import Note
from datetime import datetime

class NoteService:
    def __init__(self, db: Session):
        self.db = db

    def create_note(self, title: str, content: str, tags: str = "") -> Note:
        note = Note(title=title, content=content, tags=tags)
        self.db.add(note)
        self.db.commit()
        self.db.refresh(note)
        return note

    def get_note(self, note_id: int) -> Note:
        return self.db.query(Note).filter(Note.id == note_id).first()

    def get_all_notes(self):
        return self.db.query(Note).all()

    def update_note(self, note_id: int, title: str, content: str, tags: str) -> Note:
        note = self.get_note(note_id)
        if note:
            note.title = title
            note.content = content
            note.tags = tags
            note.updated_at = datetime.utcnow()
            self.db.commit()
            self.db.refresh(note)
        return note

    def delete_note(self, note_id: int) -> bool:
        note = self.get_note(note_id)
        if note:
            self.db.delete(note)
            self.db.commit()
            return True
        return False