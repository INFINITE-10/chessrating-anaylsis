import json, time, requests
from pathlib import Path

# API URLS 
base_url = "https://api.chess.com/pub/"
User_Agent = {
    "User-Agent" : "chessrating (contact : petersundaram6@gmail.com)",
    
}
cache_path = ""
request_delay = 1