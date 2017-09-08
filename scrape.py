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


def score_to_rate(rate_base, score):
	if score >= 1007500 :
		rate = rate_base + 2.0
	elif score >= 1005000:
		rate = rate_base + 1.5 + (score - 1005000) * 10 / 50000
	elif score >= 1000000:
		rate = rate_base + 1.0 + (score - 1000000) *  5 / 50000
	elif score >=  975000:
		rate = rate_base + 0.0 + (score -  975000) *  2 / 50000
	elif score >=  950000:
		rate = rate_base - 1.5 + (score -  950000) *  3 / 50000
	elif score >=  925000:
		rate = rate_base - 3.0 + (score -  925000) *  3 / 50000
	elif score >=  900000:
		rate = rate_base - 5.0 + (score -  900000) *  4 / 50000
	else:
		rate = 0

	return math.floor(rate * 100) / 100



# 定数情報を保管
with urllib.request.urlopen("https://chuniviewer.net/api/GetMusicConstantValues.php") as res:
	html = res.read().decode("utf-8")
	ratelist_json = json.loads(html)

html_file = ("/Users/uu071978/rate/rate/uni-scrape/html/chunithm.html")
html = codecs.open(html_file, 'r', 'utf-8')
soup = BeautifulSoup(html, "html.parser")
article = soup.find_all(class_="w388 musiclist_box bg_master")

for a in article:
	music_data = a.find(class_="music_title")
	music_id = re.search('musicId_(\d+)', str(music_data))

	highscore  = a.find(class_="text_b")
	if highscore is None:
		pass
	else:
		for music_info in ratelist_json:
			if music_id.group(1)  == str(music_info["music_id"]) and music_info["difficulty_id"] == 3 and music_info["value"] is not None:
				rate = score_to_rate(music_info["value"], int(highscore.text.replace(',', '')))
				print (music_data.text)
				print (rate)
				#print (music_data.text + " baserate is " +  str(music_info["value"]))
				#print (music_data.text + " highscore is " +  highscore.text)


		#print (music_data + " score is " + str(highscore.text))





