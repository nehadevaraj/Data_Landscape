import base64
import webbrowser
from urllib.parse import urlencode
import random
client_id = "bf9ae963bd6e4ba399cb411df7c2ed27"
client_secret = "ef91f6595ba14e36b834f348d3acf68d"

SCOPES = [
        "user-read-private",
        "user-read-email",
        "user-top-read",
        "user-follow-read"
    ]

auth_headers = {
    "client_id": client_id,
    "response_type": "code",
    "redirect_uri": "http://localhost:3000",
    "scope": " ".join(SCOPES),
    "state": random.randint(0,16)
}

webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))