from urllib.request import build_opener, HTTPCookieProcessor
from urllib.parse import urlencode
from http.cookiejar import CookieJar

import json
import pandas as pd

request_url = "https://chunithm-net.com/mobile/"

opener = build_opener(HTTPCookieProcessor(CookieJar()))

post = {
    'name': "rate0621",
    'password': "okasini0",
    'sega_login': "sega_login"
}
data = urlencode(post).encode('utf-8')

res = opener.open(request_url, data)

print (res.read().decode('utf-8'))
