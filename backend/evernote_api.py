import evernote.edam.userstore.constants as UserStoreConstants  
from evernote.api.client import EvernoteClient  

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