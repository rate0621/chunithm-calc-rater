# -*- coding: utf-8 -*-

import codecs
import re, pprint
import urllib.request
import json
import math
from bs4 import BeautifulSoup
import sys

def pp(obj):
  pp = pprint.PrettyPrinter(indent=4, width=160)
  str = pp.pformat(obj)
  return re.sub(r"\\u([0-9a-f]{4})", lambda x: unichr(int("0x"+x.group(1), 16)), str)

## 定数情報を保管
#with urllib.request.urlopen("https://chuniviewer.net/api/GetMusicConstantValues.php") as res:
# html = res.read().decode("utf-8")
# ratelist_json = json.loads(html)

html_file = ("/Users/ebinareito/rate/uni-tools/html/playlog.html")
html = codecs.open(html_file, 'r', 'utf-8')
soup = BeautifulSoup(html, "html.parser")
article = soup.find_all(class_="frame02 w400")

play_log_dict = []
for a in article:
  print (a)
  sys.exit()
  #print (a.find(class_="play_musicdata_title").text)
  #music_data = a.find(class_="music_title")
  #music_id = re.search('musicId_(\d+)', str(music_data))

  val = {
    "music_name": a.find(class_="play_musicdata_title").text,
    "score": a.find(class_="play_musicdata_score_text").text.replace('Score：', ''),
    "play_date": a.find(class_="play_datalist_date").text
  
  }
  play_log_dict.append(val)
  print (play_log_dict)
  sys.exit()




#
#	highscore  = a.find(class_="text_b")
#	if highscore is None:
#		pass
#	else:
#		for music_info in ratelist_json:
#			if music_id.group(1)  == str(music_info["music_id"]) and music_info["difficulty_id"] == 3 and music_info["value"] is not None:
#				rate = score_to_rate(music_info["value"], int(highscore.text.replace(',', '')))
#				print (music_data.text)
#				print (rate)
#				#print (music_data.text + " baserate is " +  str(music_info["value"]))
#				#print (music_data.text + " highscore is " +  highscore.text)
#
#
#		#print (music_data + " score is " + str(highscore.text))





