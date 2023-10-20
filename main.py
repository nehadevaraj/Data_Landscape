
from requests import post, get
import json
#import pandas as pd
#import numpy as np
#reading key values
import base64

#dotenv_path = find_dotenv()


client_id= "bf9ae963bd6e4ba399cb411df7c2ed27"
client_secret= "ef91f6595ba14e36b834f348d3acf68d"

#print(client_id,client_secret) #print statement for testing
def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result  = json.loads(result.content) #load script
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer "+ token}


def search_for_user(token):
    url = "https://api.spotify.com/v1/me"
    headers = get_auth_header(token)
    #query = f"?q={user_name}&type=name&limit=1"

    query_url = url# + query
    result = get(query_url, headers=headers)
    json_result  = json.loads(result.content)
    print(json_result)
def searchForArtists(token, name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    result = get(url+"?q=%s&type=artist&limit=1" %(name),headers=headers)
    json_result = json.loads(result.content)
    print(json_result)
get_token()
token = get_token()
print(token)
print(get("https://api.spotify.com/v1/me",headers=get_auth_header(token)))
searchForArtists(token,"ACDC")


