import pandas as pd
 
data_frame = pd.DataFrame(index=[], columns=['column1', 'column2'])
series = pd.Series(['hoge', 'fuga'], index=data_frame.columns)
 
for i in range(5):
   data_frame = data_frame.append(series, ignore_index = True)
     
data_frame.to_csv("aaa.csv", index=False)
