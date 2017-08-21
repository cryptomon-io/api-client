import requests
import json

OAUTH_TOKEN_URL = "https://api.cryptomon.io/oauth/token"

class ApiClient:
    
    client_id = None
    client_secret = None
    
    access_token = None
    
    def __init__(self, client_id, client_secret):
        self.client_id = client_id;
        self.client_secret = client_secret;
    
    def request_access(self):
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials"
        }        
        headers = {
        }
        
        print("Requesting access_token...")
        r = requests.post(OAUTH_TOKEN_URL, data=data, headers=headers)
        
        if r.status_code == 200:            
            result = json.loads(r.text)
            self.access_token = result["access_token"]
            print("Success, access_token: " + self.access_token + ", expires_in: " + str(result["expires_in"]))
        else:
            print("Fail, status_code: " + str(r.status_code) + ", result: " + r.text)
            self.access_token = None
            
    def get(self, url, params):        
        if self.access_token == None:
            print("Empty access_token in header!")
            return
                
        headers = {
            "Content-type": "application/json",
            "Authorization": "Bearer " + self.access_token
        }
        
        print("Request, url: " + url + ", params: " + str(params))
        r = requests.get(url, params=params, headers=headers)
        
        if r.status_code == 200:
            print("Success, status_code: 200");
            result = json.loads(r.text)
            return result
        else:
            print("Fail, status_code: " + str(r.status_code) + ", result: " + r.text)
            return None
        