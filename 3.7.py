s = input('Введите строку: ')

for i in s:
    print(f"Код символа '{i}' в Юникоде: {ord(i)}")
    print(f"Код символа '{i}' в ASCII: {ascii(i)}")