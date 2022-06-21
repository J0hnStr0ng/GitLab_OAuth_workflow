import html
import json
import os
import re
import urllib.parse
import requests
import pprint

provider = "https://gitlab.com/oauth/token?"
client_id = "{your_client_id_here}"
client_secret = "{your_client_secret}"
code = "{your_generated_code}"
redirect_url = "{your_url_here}"

resp = requests.get(
  url = provider,
  params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "code": code,
    "grant_type": "authorization_code",
    "redirect_url": redirect_url,
  },
  allow_redirects=False
)
resp.json()
