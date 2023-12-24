def lower(s):
    return chr(ord(s) + 32)
def upper(s):
    return chr(ord(s) - 32)

s = input("Введите символ: ")

try:
    if 65 <= ord(s) <= 90 or 1040 <= ord(s) <= 1071:
        print(lower(s))

    elif 97 <= ord(s) <= 122 or 1072 <= ord(s) <= 1103:
        print(upper(s))

    # Ё находится отдельно от всех символов
    elif ord(s) == 1105:
        print("Ё")
    elif ord(s) == 1025:
        print("ё")

except:
    print('Введен не верный символ')
