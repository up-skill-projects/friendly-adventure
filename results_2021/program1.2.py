""" калькулятор обнуляющие биты """
act = input("Какое действие будем выполнять? ")
""" калькулятор обнуляющие биты """
MY_STR = ''
division = 2
if act == '^':
    number = int(input("введите число => "))
    second = int(input("В какую степень будем возводить? "))
    print("Результат =>", number**second)
elif act == '!':
    number = int(input("Введите число=> "))
    bits = int(input('число бит: '))
    while number > 0:
        if bits and number % division:
            MY_STR = '0' + MY_STR
            bits -= 1
        else:
            MY_STR = str(number % division) + MY_STR
        number = number // division
    print("Результат=>", int(MY_STR, division))
else:
    print('Не верное действие!')
