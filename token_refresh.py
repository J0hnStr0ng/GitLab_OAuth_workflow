import html
import json
import os
import re
import urllib.parse
import requests
import pprint

provider = "https://gitlab.com/oauth/token?"
client_id = "{your_client_id_here}"
refesh_token = "{your_refresh_token}" #pulled from the initial auth
redirect_url = "{your_url_here}"

resp = requests.get(
  url = provider,
  params = {
    "client_id": client_id,
    "refesh_token": refresh_token,
    "grant_type": "refesh_token",
    "redirect_url": redirect_url,
  },
  allow_redirects=False
)
resp.json()
