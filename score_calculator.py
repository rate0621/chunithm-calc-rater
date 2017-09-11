import sys
import urllib.request
import json
import math
import pandas as pd

import ChunithmNet


class ScoreCalculator:
  def __init__(self):
    pass


  def score_to_rate(self, score, base_rate):
    if score >= 1007500 :
      rate = base_rate + 2.0
    elif score >= 1005000:
      rate = base_rate + 1.5 + (score - 1005000) * 10 / 50000
    elif score >= 1000000:
      rate = base_rate + 1.0 + (score - 1000000) *  5 / 50000
    elif score >=  975000:
      rate = base_rate + 0.0 + (score -  975000) *  2 / 50000
    elif score >=  950000:
      rate = base_rate - 1.5 + (score -  950000) *  3 / 50000
    elif score >=  925000:
      rate = base_rate - 3.0 + (score -  925000) *  3 / 50000
    elif score >=  900000:
      rate = base_rate - 5.0 + (score -  900000) *  4 / 50000
    else:
      rate = 0

    return math.floor(rate * 100) / 100

  def create_baserate_list(self):
    with urllib.request.urlopen("https://chuniviewer.net/api/GetMusicConstantValues.php") as res:
      html = res.read().decode("utf-8")
      ratelist_json = json.loads(html)

    ## 負荷軽減のため
    ## {  
    ##   key1: {aaa: "hoge", bbb: "weei"},
    ##   key2: {aaa: "huge", bbb: "fooo"}
    ## }
    ## の形式になるように整形
    baserate_list = {}
    for music_info in ratelist_json:
      key = str(music_info["music_id"]) + "_" + str(music_info["difficulty_id"])
      baserate_list[key] = music_info

    return baserate_list


  def calc_rate(self, baserate_list, my_score):
    for key in my_score:
      my_score[key]["rate"] = 0
      if my_score[key]["score"] == 0:
        print (my_score[key]["music_name"] + " is not play...")
      else:
        if baserate_list[key]["value"] == None:
          print ("Sorry, " + my_score[key]["music_name"] + " baserate is None.")
        else:
          rate = self.score_to_rate(int(my_score[key]["score"].replace(',', '')), baserate_list[key]["value"])
          my_score[key]["rate"] = rate

    return my_score


  def calc_rate(self, score, playlog):
    """
    与えられた変数score, playlogから算出した平均値を返す
    score -> best枠として上位20位の楽曲
    playlog -> recent枠として上位10位の楽曲

    best、recentの30曲のrateの平均値がrateとなる。
    """

    best_music_limit = 20
    rate_array = []
    for i, key in enumerate(sorted(my_rate, key=lambda x:my_rate[x]["rate"], reverse=True)):
      rate_array.append(my_rate[key]["rate"])
      if i == best_music_limit - 1:
        break

    average = sum(rate_array)/len(rate_array)

    return math.floor(average * 100) / 100
    
    
if __name__ == '__main__':
  sc = ScoreCalculator()
  baserate_list = sc.create_baserate_list()

  args = sys.argv
  cn = ChunithmNet.ChunithmNet(args[1], args[2])
  score, playlog = cn.get_score_and_playlog()
  rate = sc.calc_rate(baserate_list, score, playlog)
  print (sc.calc_my_bests(my_rate))


