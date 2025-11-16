import pandas as pd
df = pd.read_csv('pandas_libs//power.csv', encoding= 'utf-8')

summa = df.query('category in (4, 12, 21) and year > 2004 and year < 2011 and quantity > 0 and country in (\'Latvia\', \'Estonia\', \'Litva\')')['quantity'].sum()

print(f'Cуммарное потребление стран Прибалтики: {summa}')

