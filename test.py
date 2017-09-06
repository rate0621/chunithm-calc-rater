
import sys
import json

f = open('/Users/uu071978/rate/rate/uni-scrape/html/ratelist.php', 'r')

json_dict = json.load(f)
#print('json_dict:{}'.format(type(json_dict[0])))
#json_str = json.dumps(json_dict)
#print('json_str:{}'.format(type(json_str)))

for a in json_dict:
	print (a)
#	sys.exit()

