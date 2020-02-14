#!/usr/bin/env python3

"""
This script gets a random featured image from unsplash.com and sets it as your desktop background. Works on `gsettings` supported linux distros. Tested on Ubuntu 19.10 (Gnome). Requires the `requests` module to be installed.

It takes some time to download the photo. So, wait patiently after executing the script.

You can use `anacrontab` to run it daily or weekly. See http://bit.ly/371ybhq
"""

import requests
import os
from os import system
from datetime import datetime

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Create an app here: https://unsplash.com/oauth/applications
# and collect your client_id
with open('key', 'r') as f:
    client_id = f.read().strip()


def unsplash(path, **params):
    return requests.get('https://api.unsplash.com' + path, params={'client_id': client_id, **params})


res = unsplash('/photos/random', featured=True, orientation='landscape')

img = res.json()

url = img['urls']['regular']

with open('log.txt', 'a') as f:
    print(
        f"{datetime.now().strftime('%d %b %Y %H:%M')}\n{img['description']}\n{img['location']['name']}\n{img['links']['html']}\n", file=f)

system(f'gsettings set org.gnome.desktop.background picture-uri {url}')
