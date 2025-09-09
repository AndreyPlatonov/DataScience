queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт кино',
]
user_request = {} 

# переопределяем список заменяя значения элементов на число слов в элементе
for i in range(len(queries)):
    queries[i] = len(queries[i].split(' '))   

# заполняем словарь , ключ уникальные элементы, значение число повторений элемента 
for l in queries:    
    user_request[l] = queries.count(l)
# вывод
for u_key, u_value in user_request.items():
    print(f'Поисковых запросов, содержащих {u_key} слов(а): {round(u_value/len(queries)*100, 2)}%')
