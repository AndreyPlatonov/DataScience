import pandas as pd

geo_data = {

          'Центр': ['москва', 'тула', 'ярославль'],

          'Северо-Запад': ['петербург', 'псков', 'мурманск'],

          'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск'] 
           }

def regionName(keyword):
    
    for key, value in geo_data.items():
        
        for values in value:
            
            if values in keyword.lower():
                
               return key
           
    
    
    return 'undefined'

keywords = pd.read_csv('functions_and_work_data//keywords.csv')

keywords['region'] = keywords['keyword'].apply(regionName)

print(f'Гео-классификатор по ключевым словам:  \n{keywords}')




