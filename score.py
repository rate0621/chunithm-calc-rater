# -*- coding: utf-8 -*-

import codecs
import re, pprint
import urllib.request
import json
import math
from bs4 import BeautifulSoup
import sys

html_file = ("/Users/ebinareito/rate/uni-tools/html/chunithm.html")
html = codecs.open(html_file, 'r', 'utf-8')
soup = BeautifulSoup(html, "html.parser")

article = soup.find_all(class_="w388 musiclist_box bg_master")
my_records = {}
for a in article:
  music_data = a.find(class_="music_title")
  music_id = re.search('musicId_(\d+)', str(music_data))
  highscore  = a.find(class_="text_b")

  # TODO: とりあえずMASTERのスコアだけをとるため3を直接書いている
  #       いずれはMASTERとEXPERT（もしくは全部）を取ってくるようにする
  key = str(music_id.group(1)) + "_" + "3"
  if highscore is None:
    my_records[key] = {"music_id": music_id.group(1), "music_name": music_data.text, "difficulty_id": "3", "score": 0}
  else:
    my_records[key] = {"music_id": music_id.group(1), "music_name": music_data.text, "difficulty_id": "3", "score": highscore.text}

  #print (my_records[key])


html_file = ("/Users/ebinareito/rate/uni-tools/html/playlog.html")
html = codecs.open(html_file, 'r', 'utf-8')
soup = BeautifulSoup(html, "html.parser")
article = soup.find_all(class_="frame02 w400")

play_log_dict = []
for a in article:
  #print (a)
  #sys.exit()
  #print (a.find(class_="play_musicdata_title").text)
  #music_data = a.find(class_="music_title")
  #music_id = re.search('musicId_(\d+)', str(music_data))

  val = {
    "music_name": a.find(class_="play_musicdata_title").text,
    "score": a.find(class_="play_musicdata_score_text").text.replace('Score：', ''),
    "play_date": a.find(class_="play_datalist_date").text

  }
  play_log_dict.append(val)
  #print (play_log_dict)

#print (len(play_log_dict))
#sys.exit()

for row in play_log_dict:
  search_str = row["music_name"]
  for key, val in my_records.items():
    if val["music_name"] == search_str:
      print ("search!")
      break

  #print (search_str)

