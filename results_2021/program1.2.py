act = input("Какое действие будем выполнять? ")
strings = ''
if act == '^':
    number = int(input("введите число => "))
    second = int(input("В какую степень будем возводить? "))
    print("Результат =>", number**second)
elif act == '!':
    number = int(input("Введите число=> "))
    bits = int(input('число бит: '))
    while number > 0:
        if bits and number % 2:
            strings = '0' + strings
            bits -= 1
        else:
            strings = str(number % 2) + strings
        number = number // 2
    print("Результат=>", int(strings, 2))
else:
    print('Не верное действие!')
