import urllib.request
with urllib.request.urlopen("http://www.yoheim.net") as res:
   html = res.read().decode("utf-8")
   print(html)
