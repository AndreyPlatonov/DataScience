# ввод дня и месяца рождения
day_of_birth = int(input("Введите день рождения: "))
month_of_birth = input("Введите месяц рождения: ").capitalize()  

# вычисляем знак зодиака

if (month_of_birth == "Март" and day_of_birth >= 21 and day_of_birth <= 31) or (month_of_birth == "Апрель" and day_of_birth <= 19 and day_of_birth >= 1):
    print('Ваш знак зодиака: Овен')
elif (month_of_birth == "Апрель" and day_of_birth >= 20 and day_of_birth <= 30) or (month_of_birth == "Май" and day_of_birth <= 20 and day_of_birth >= 1):
    print('Ваш знак зодиака: Телец')
elif (month_of_birth == "Май" and day_of_birth >= 21 and day_of_birth <= 31)  or (month_of_birth == "Июнь" and day_of_birth <= 20 and day_of_birth >= 1 ):
    print('Ваш знак зодиака: Близнецы')
elif (month_of_birth == "Июнь" and day_of_birth >= 21 and day_of_birth <= 30) or (month_of_birth == "Июль" and day_of_birth <= 22 and day_of_birth >= 1):
    print('Ваш знак зодиака: Рак')
elif (month_of_birth == "Июль" and day_of_birth >= 23 and day_of_birth <= 31) or (month_of_birth == "Август" and day_of_birth <= 22 and day_of_birth >= 1):
    print('Ваш знак зодиака: Лев')
elif (month_of_birth == "Август" and day_of_birth >= 23 and day_of_birth <= 31) or (month_of_birth == "Сентябрь" and day_of_birth <= 22 and day_of_birth >= 1):
    print('Ваш знак зодиака: Дева')
elif (month_of_birth == "Сентябрь" and day_of_birth >= 23 and day_of_birth <= 30) or (month_of_birth == "Октябрь" and day_of_birth <= 22 and day_of_birth >= 1):
    print('Ваш знак зодиака: Весы')
elif (month_of_birth == "Октябрь" and day_of_birth >= 23 and day_of_birth <= 31) or (month_of_birth == "Ноябрь" and day_of_birth <= 21 and day_of_birth >= 1):
    print('Ваш знак зодиака: Скорпион')
elif (month_of_birth == "Ноябрь" and day_of_birth >= 22 and day_of_birth <= 30) or (month_of_birth == "Декабрь" and day_of_birth <= 21 and day_of_birth >= 1):
    print('Ваш знак зодиака: Стрелец')
elif (month_of_birth == "Декабрь" and day_of_birth >= 22 and day_of_birth <= 31) or (month_of_birth == "Январь" and day_of_birth <= 19 and day_of_birth >= 1):
    print('Ваш знак зодиака: Козерог')
elif (month_of_birth == "Январь" and day_of_birth >= 20 and day_of_birth <= 31) or (month_of_birth == "Февраль" and day_of_birth <= 18 and day_of_birth >= 1):
    print('Ваш знак зодиака: Водолей')
elif (month_of_birth == "Февраль" and day_of_birth >= 19 and day_of_birth <= 29) or (month_of_birth == "Март" and day_of_birth <= 20 and day_of_birth >= 1):
    print('Ваш знак зодиака: Рыбы')
else:
    print('данные введены некорректно')