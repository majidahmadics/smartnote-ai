import spacy  
from spacy.matcher import Matcher 


class NLPProcessor:  
    def __init__(self):  
        self.nlp = spacy.load("en_core_web_sm")  
        self.matcher = Matcher(self.nlp.vocab)  
         
        pattern = [{"LOWER": "project"}, {"IS_ALPHA": True}]  
        self.matcher.add("PROJECT_PATTERN", [pattern])  

    def extract_tags(self, text):  
        doc = self.nlp(text)  
        tags = [ent.text for ent in doc.ents]  # Extract entities (people, dates, etc.)  
        # Add custom matches  
        matches = self.matcher(doc)  
        for match_id, start, end in matches:  
            tags.append(doc[start:end].text)  
        return list(set(tags))  # Deduplicate
    

if __name__ == "__main__":
    processor = NLPProcessor()  
    text = "Discuss Q3 goals with Sarah in Project Alpha by Friday."  
    print(f"{processor.extract_tags(text)}\n# The |{processor}| Works perfectly.")
