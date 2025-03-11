import evernote.edam.userstore.constants as UserStoreConstants  
from evernote.api.client import EvernoteClient  
from models import Note, Session
from nlp_processor import NLPProcessor

class EvernoteAuth:  
    def __init__(self):  
        self.consumer_key = "YOUR_KEY"  
        self.consumer_secret = "YOUR_SECRET"  
        self.callback_url = "http://localhost:5000/oauth_callback"  
        self.client = EvernoteClient(  
            consumer_key=self.consumer_key,  
            consumer_secret=self.consumer_secret,  
            sandbox=True  # Use Evernote's sandbox environment  
        )  

    def get_request_token(self):  
        return self.client.get_request_token(self.callback_url)  

    def get_authorize_url(self, request_token):  
        return self.client.get_authorize_url(request_token)  
    

class EvernoteClient:  
    def __init__(self):  
        self.auth = EvernoteAuth()  
        self.nlp = NLPProcessor()  

    def fetch_and_process_notes(self):  
        note_store = self.auth.client.get_note_store()  
        notes = note_store.listNotes()  
        session = Session()  
        for note in notes:  
            tags = self.nlp.extract_tags(note.content)  
            db_note = Note(  
                evernote_id=note.guid,  
                title=note.title,  
                content=note.content,  
                tags=",".join(tags),  
                created_at=note.created  
            )  
            session.add(db_note)  
        session.commit()  