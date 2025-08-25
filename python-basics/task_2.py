# вводим значение года

year_check=int(input('Введите год: '))

# условие проверки на високосный год
check_year=(year_check % 400 ==0 or (year_check % 4 ==0 and year_check % 100 >0))

if check_year:
  print('Високосный год')
else:
  print('Обычный год')  
