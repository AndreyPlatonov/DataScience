import pandas as pd

movies = pd.read_csv('pandas_libs//movies.csv')
ratings = pd.read_csv('pandas_libs//ratings.csv')

ratingsTop=ratings[ratings.rating == 5].movieId.value_counts().head(1)

movieTop = pd.merge(ratingsTop, movies, on = 'movieId', how = 'left')


print(f'этому фильму было выставлено больше всего оценок 5.0: \n{movieTop.title.squeeze()}')

