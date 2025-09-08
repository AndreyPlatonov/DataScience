string_word=input('Введите строку: ')

# остаток деления длины строки на 2
parity = len(string_word) % 2

# частное деления длины строки на 2
div = len(string_word) // 2

if parity == 0 :
   print(string_word[div-1:div+1])
else:
   print(string_word[div])
    