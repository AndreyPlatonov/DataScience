# вводим данные размеров товара
product_weight = int(input('Введите ширину товара в см: '))
product_length = int(input('Введите длину товара в см: '))
product_height = int(input('Введите высоту товара в см: '))

if (product_height <= 15 and product_weight <= 15 and product_length <= 15):
    print ('Коробка № 1')
elif (product_height > 200 or product_length > 200 or product_weight > 200):
    print ('Упаковка для лыж')  
elif((product_weight > 15 and product_weight < 50) or (product_height > 15 and product_height < 50) or (product_length > 15 and product_length < 50)):
    print ('Коробка № 2')
else:
    print ('Коробка № 3')       