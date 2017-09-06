# -*- coding: utf-8 -*-

import codecs
import re, pprint
from bs4 import BeautifulSoup

def pp(obj):
  pp = pprint.PrettyPrinter(indent=4, width=160)
  str = pp.pformat(obj)
  return re.sub(r"\\u([0-9a-f]{4})", lambda x: unichr(int("0x"+x.group(1), 16)), str)

html_file = ("/Users/uu071978/rate/rate/uni-scrape/html/chunithm.html")
html = codecs.open(html_file, 'r', 'utf-8')
soup = BeautifulSoup(html, "html.parser")
article = soup.find(class_="box02 w420 mb_20")
option = article.find_all("option")

print (pp(option))
