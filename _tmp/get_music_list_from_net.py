# -*- coding: utf-8 -*-

from time import sleep
import codecs
import re, pprint
import urllib.request
import json
import math
from bs4 import BeautifulSoup
import sys, os
import http.cookiejar
import pandas as pd


## login
args = sys.argv
name = args[1]
password = args[2]

cookiefile = "cookies.txt"
cj = http.cookiejar.LWPCookieJar()
if os.path.exists(cookiefile):
    cj.load(cookiefile)
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)

headers = {
      "Accept" :"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
      "Accept-Encoding" :"gzip, deflate, br",
      "Accept-Language" :"ja,en-US;q=0.8,en;q=0.6",
      "Cache-Control" :"max-age=0",
      "Connection" :"keep-alive",
      "Content-Length" :"70",
      "Content-Type" :"application/x-www-form-urlencoded"
}

login_url = "https://chunithm-net.com/mobile/"
login_post = {
  'segaId': name,
  'password': password,
  'save_cookie': "on",
  'sega_login': "sega_login"
}
data = urllib.parse.urlencode(login_post).encode("utf-8")

req = urllib.request.Request(login_url, None, headers)
with urllib.request.urlopen(req, data=data) as res:
  res.close()

# login画面の先のaime選択画面の突破
aime_url = "https://chunithm-net.com/mobile/AimeList.html"
aime_post = {
  'aimeIndex': "0",
  'aimelogin': "aimelogin",
  'aime_login_0': "aime_login_0"
}
data = urllib.parse.urlencode(aime_post).encode("utf-8")

req = urllib.request.Request(aime_url, None, headers)
with urllib.request.urlopen(req, data=data) as res:
  res.close()

html_file = ("/Users/ebinareito/rate/uni-tools/html/chunithm.html")
html = codecs.open(html_file, 'r', 'utf-8')
soup = BeautifulSoup(html, "html.parser")
article = soup.find_all(class_="w388 musiclist_box bg_master")

# 定数情報を保管
with urllib.request.urlopen("https://chuniviewer.net/api/GetMusicConstantValues.php") as res:
  html = res.read().decode("utf-8")
  ratelist_json = json.loads(html)
  res.close()

df = pd.DataFrame(
  columns = ['music_id', 'music_name', "difficulty_id", "difficulty", 'baserate', 'img_filename']
)

for a in article:
  music_data = a.find(class_="music_title")
  music_id = re.search('musicId_(\d+)', str(music_data))

  sleep(3)
  ## 曲詳細画面拾得
  url = "https://chunithm-net.com/mobile/MusicGenre.html"
  get_score_post = {
    'musicId': music_id.group(1),
    'music_detail': "music_detail"
  }
  data = urllib.parse.urlencode(get_score_post).encode("utf-8")

  req = urllib.request.Request(url, None, headers)
  with urllib.request.urlopen(req, data=data) as res:
    html = res.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    hogehoge = soup.find(class_="play_jacket_img")
    img_filename = hogehoge.find("img").get("src")
    #print (img_filename)
    res.close()

  for music_info in ratelist_json:
    if int(music_info["music_id"]) == int(music_id.group(1)):
      series = pd.Series([music_info["music_id"], music_info["music_name"], music_info["difficulty_id"], music_info["level"], music_info["value"], img_filename], index=df.columns)
      df = df.append(
        series, ignore_index = True
      )
      print (str(music_info["music_id"]) + "  " + str(music_info["music_name"]) + "  " + str(music_info["difficulty_id"]) + "  " + str(music_info["level"]) + "  " + str(music_info["value"]) + "  " + str(img_filename))



df.to_csv("base_rate.csv", index=False)
######

