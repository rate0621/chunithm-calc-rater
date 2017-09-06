import urllib.request
import json
import pandas as pd

with urllib.request.urlopen("https://chuniviewer.net/api/GetMusicConstantValues.php") as res:
	html = res.read().decode("utf-8")
	ratelist_json = json.loads(html)


df = pd.DataFrame(
	index=[],
	columns = ['name', 'rate']
)

for music_info in ratelist_json:
	series = pd.Series([music_info["music_id"], music_info["music_name"]], index=df.columns)

	df = df.append(
		series, ignore_index = True
	)


#data_frame = pd.DataFrame(index=[], columns=['column1', 'column2'])
#series = pd.Series(['hoge', 'fuga'], index=data_frame.columns)
#
#for i in range(5):
#   data_frame = data_frame.append(series, ignore_index = True)
#
#data_frame.to_csv("aaa.csv", index=False)

df.to_csv("employee.csv", index=False)
