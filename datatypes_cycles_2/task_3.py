results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}


for results_value in results.values():
    # добавление нового ключа в словарь значений исходного словаря
    revenue = results_value['revenue']
    cost = results_value['cost']
    results_value['ROI'] = round(((revenue / cost) - 1) * 100, 2)
# вывод  
print (results)