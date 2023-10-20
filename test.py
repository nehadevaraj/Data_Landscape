
import base64
import webbrowser
from urllib.parse import urlencode

client_id = "bf9ae963bd6e4ba399cb411df7c2ed27"
client_secret = "ef91f6595ba14e36b834f348d3acf68d"

SCOPES = [
        'ugc-image-upload',
        'user-read-playback-state',
        'user-top-read',
        'user-read-recently-played',
        'playlist-read-private',
        'user-read-currently-playing'
    ]

auth_headers = {
    "client_id": client_id,
    "response_type": "code",
    "redirect_uri": "http://localhost:3000",
    "scope": " ".join(SCOPES)
}

webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))