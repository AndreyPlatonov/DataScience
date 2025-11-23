import pandas as pd


ratings = pd.read_csv('advanced_pandas//ratings.csv', encoding='utf8')

def groupby_function(data):
    
    return data.timestamp.max() - data.timestamp.min()

rating_200 = ratings.groupby(['userId']).filter(lambda x: len(x) > 200)
rating_life_time = rating_200.groupby(['userId']).apply(groupby_function)

print(f' среднее время жизни пользователей, которые выставили более 100 оценок: \n{rating_life_time.head()}')