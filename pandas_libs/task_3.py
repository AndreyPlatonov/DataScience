import pandas as pd

page_url = 'https://www.nalog.gov.ru/opendata/7707329152-kalendar/'

df = pd.read_html(page_url, attrs = {'class': 'border_table'}, encoding = 'utf-8')

print(f'Дата фрейм: \n {df}')

