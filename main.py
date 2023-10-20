
#import requests
#import pandas as pd
#import numpy as np

from dotenv import load_dotenv #reading key values
import os

#dotenv_path = find_dotenv()
load_dotenv()

client_id= os.getenv("CLIENT_ID")
client_secret= os.getenv("CLIENT_SECRET")

print(client_id,client_secret) #print statement

#POST "https://accounts.spotify.com/api/token" \