ids = {'user1': [213, 213, 213, 15, 213], 
       'user2': [54, 54, 119, 119, 119], 
       'user3': [213, 98, 98, 35]}

answer = set() # результирующее множество
for values_ids in ids.values():
    answer=answer.union(set(values_ids))  # в цикле обьединяем множества для удаления дублей

# вывод   
print(answer)   
