phrase_1 = str(input('Введите строку 1'))
phrase_2 = str(input('Введите строку 1'))

if len(phrase_1) > len(phrase_2):
    print('Фраза 1 длиннее фразы 2')
    print(phrase_1)
    print(phrase_2)
elif  len(phrase_1) < len(phrase_2):
    print('Фраза 2 длиннее фразы 1')
    print(phrase_1)
    print(phrase_2)
else :
    print('Фразы равной длины')    
