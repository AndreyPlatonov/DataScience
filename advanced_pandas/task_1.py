import pandas as pd

logs = pd.read_csv('advanced_pandas//visit_log.csv')

def sourceLog(row) :
  
  row = row.tolist()[0].split(';') 
  
  if row[5] in ['yandex', 'google']:
       return 'orhanic'
  elif  row[5] in ['yandex', 'google'] and row[3] == 'Russia':
       return 'ad'
  elif  row[5] in ['yandex', 'google']  and row[3] != 'Russia':
       return 'other'
  else:
       return row[5]

logs['source_type'] = logs.apply(sourceLog, axis =1)

print(f' Датафрейм c добавленным столбцом source_type :\n{logs.head()}')