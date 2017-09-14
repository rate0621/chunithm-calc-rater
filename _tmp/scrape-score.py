import urllib.request
import json
import pandas as pd

with urllib.request.urlopen("https://chuniviewer.net/api/GetMusicConstantValues.php") as res:
	html = res.read().decode("utf-8")
	ratelist_json = json.loads(html)


df = pd.DataFrame(
	columns = ['MUSICID', 'MUSICNAME', "difficulty_id", "level", 'BASERATE']
)

for music_info in ratelist_json:
	series = pd.Series([music_info["music_id"], music_info["music_name"], music_info["difficulty_id"], music_info["level"], music_info["value"]], index=df.columns)

	df = df.append(
		series, ignore_index = True
	)

df.to_csv("base_rate.csv", index=False)
