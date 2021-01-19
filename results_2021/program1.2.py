""" калькулятор обнуляющие биты """
act = input("Какое действие будем выполнять? ")
""" калькулятор обнуляющие биты """
MY_STR = ''
NUMBER_TWO = 2
if act == '^':
    number = int(input("введите число => "))
    second = int(input("В какую степень будем возводить? "))
    print("Результат =>", number**second)
elif act == '!':
    number = int(input("Введите число=> "))
    bits = int(input('число бит: '))
    while number > 0:
        if bits and number % NUMBER_TWO:
            MY_STR = '0' + MY_STR
            bits -= 1
        else:
            MY_STR = str(number % NUMBER_TWO) + MY_STR
        number = number // NUMBER_TWO
    print("Результат=>", int(MY_STR, NUMBER_TWO))
else:
    print('Не верное действие!')
