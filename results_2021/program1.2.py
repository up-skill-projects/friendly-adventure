act = input("Какое действие будем выполнять? ")
""" калькулятор обнуляющие биты """
my_strings = ''
two = 2
if act == '^':
    number = int(input("введите число => "))
    second = int(input("В какую степень будем возводить? "))
    print("Результат =>", number**second)
elif act == '!':
    number = int(input("Введите число=> "))
    bits = int(input('число бит: '))
    while number > 0:
        if bits and number % two:
            my_strings = '0' + my_strings
            bits -= 1
        else:
            my_strings = str(number % two) + my_strings
        number = number // two
    print("Результат=>", int(my_strings, two))
else:
    print('Не верное действие!')
