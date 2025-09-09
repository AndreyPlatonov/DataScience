stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 120, 'email': 42, 'ok': 98}

# вычисляем максимальный обьем продаж
max_sale=max(stats.values())

# вычисляем ключи словаря с максимальными продажами
keys= [key for key, value in stats.items() if value == max_sale]

# вывод
for key in keys:
    print(f'Максимальный объем продаж на рекламном канале: {key}')
