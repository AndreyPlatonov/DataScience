import pandas as pd

df = pd.read_csv('advanced_pandas//URLs.txt', encoding='utf8')

news = df[df.url.str.contains('/\d{8}-', regex = True)]

print(f' Датафрейм новостей: \n{news.head()}')