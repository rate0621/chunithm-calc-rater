import urllib.request
from operator import itemgetter
import json
import pandas as pd

hoge = {
    "a": { "rate": 1},
    "b": { "rate": 999},
    "c": { "rate": 30},
    "d": { "rate": 9}
}


#sorted(tasks, key=lambda x:x['TaskId'])
for a in sorted(hoge, key=lambda x:hoge[x]["rate"]):
    print (hoge[a])

#l2 = sorted(hoge, key=lambda x:hoge[x]["rate"])
#print (l2)
