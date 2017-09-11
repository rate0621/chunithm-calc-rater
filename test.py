import urllib.request
import json
import sys

with urllib.request.urlopen("https://chuniviewer.net/api/GetMusicConstantValues.php") as res:
  html = res.read().decode("utf-8")
  ratelist_json = json.loads(html)


for hoge in ratelist_json:
	print (hoge["value"])
	sys.exit()
