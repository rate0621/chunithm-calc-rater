# -*- coding: utf-8 -*-

import codecs
import re, pprint
from bs4 import BeautifulSoup
import sys

def pp(obj):
  pp = pprint.PrettyPrinter(indent=4, width=160)
  str = pp.pformat(obj)
  return re.sub(r"\\u([0-9a-f]{4})", lambda x: unichr(int("0x"+x.group(1), 16)), str)

html_file = ("/Users/uu071978/rate/rate/uni-scrape/html/chunithm.html")
html = codecs.open(html_file, 'r', 'utf-8')
soup = BeautifulSoup(html, "html.parser")
article = soup.find_all(class_="w388 musiclist_box bg_master")

for a in article:
	print (a.find(class_="play_musicdata_highscore"))


#print (pp(article))
