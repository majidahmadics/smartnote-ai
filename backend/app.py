from flask import Flask, jsonify  
from evernote_api import EvernoteClient
from models import Note, Session

app = Flask(__name__)  

@app.route("/api/notes")  
def get_processed_notes():  
    client = EvernoteClient()  
    # Fetch notes from DB (simplified)  
    session = Session()  
    notes = session.query(Note).all()  
    return jsonify([{"title": n.title, "tags": n.tags.split(",")} for n in notes])  

if __name__ == "__main__":  
    app.run(debug=True)  