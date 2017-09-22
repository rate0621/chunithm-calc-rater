#from urllib.request import build_opener, HTTPCookieProcessor
import urllib.request
from urllib.parse import urlencode
import http.cookiejar
import sys, os

import json
import pandas as pd

cookiefile = "cookies.txt"
cj = http.cookiejar.LWPCookieJar()
if os.path.exists(cookiefile):
    cj.load(cookiefile)
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)

login_url = "https://chunithm-net.com/mobile/"
aime_url = "https://chunithm-net.com/mobile/AimeList.html"
score_url = "https://chunithm-net.com/mobile/MusicGenre.html"

login_post = {
    'segaId': "",
    'password': "",
    'save_cookie': "on",
    'sega_login': "sega_login"
}

aime_post = {
    'aimeIndex': "0",
    'aimelogin': "aimelogin",
    'aime_login_0': "aime_login_0"
}

get_score_post = {
    'genre': "99",
    'level': "master",
    'music_genre': "music_genre"
}

headers = {
    "Accept" :"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding" :"gzip, deflate, br",
    "Accept-Language" :"ja,en-US;q=0.8,en;q=0.6",
    "Cache-Control" :"max-age=0",
    "Connection" :"keep-alive",
    "Content-Length" :"70",
    "Content-Type" :"application/x-www-form-urlencoded"
}

data = urllib.parse.urlencode(login_post).encode("utf-8")
req = urllib.request.Request(login_url, None, headers)
with urllib.request.urlopen(req, data=data) as res:
    html = res.read().decode("utf-8")
    res.close()


data = urllib.parse.urlencode(aime_post).encode("utf-8")
req = urllib.request.Request(aime_url, None, headers)
with urllib.request.urlopen(req, data=data) as res:
    html = res.read().decode("utf-8")
    res.close()

data = urllib.parse.urlencode(get_score_post).encode("utf-8")
req = urllib.request.Request(score_url, None, headers)
with urllib.request.urlopen(req, data=data) as res:
    html = res.read().decode("utf-8")
    print(html)




