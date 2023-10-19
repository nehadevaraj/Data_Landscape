
import requests
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv, find_dotenv #reading key values

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

pd.set_option('display.max_columns', None)

#POST "https://accounts.spotify.com/api/token" \