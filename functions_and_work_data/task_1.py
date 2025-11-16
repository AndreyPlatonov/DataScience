import pandas as pd


def ratingName(rating):
    
    if rating <= 2:
       
       return 'низкий рейтинг'
    elif rating <= 4:
       return 'средний рейтинг'
    elif rating in (4.5, 5) :
       return 'высокий рейтинг'    
    else:
       return None
   
 
     
ratings = pd.read_csv('functions_and_work_data//ratings.csv')

ratings['class'] = ratings.rating.apply(ratingName)

print(f'Обновленные рейтинги с наименованиями:  \n{ratings}')