def Cezar(message, key):
    ans = ''
    for i in range(len(message)):
        if message[i].isalpha():
            # Английский
            if ord('a') <= ord(message[i]) <= ord('z') or ord('A') <= ord(message[i]) <= ord('Z'):
                base = ord('A') if message[i].isupper() else ord('a')
                ans += chr((ord(message[i]) - base + key[i]) % 26 + base)

            # Русский
            elif ord('а') <= ord(message[i]) <= ord('я') or ord('А') <= ord(message[i]) <= ord('Я'):
                base = ord('А') if message[i].isupper() else ord('а')
                ans += chr((ord(message[i]) - base + key[i]) % 32 + base)

        else:
            ans += i
    return ans

message = input("Введите сообщение: ")
mode = input("Выберите режим: 1 или 2 (3.91 и 3.92): ")

if mode == '1':
    key_num = int(input("Введите сдвиг: "))
    key = [key_num]*len(message)
elif mode == '2':
    key = []
    for i in range(len(message)):
        key.append(int(input(f'Введите ключ для {i+1} буквы ("{message[i]}"): ')))


print(Cezar(message, key))