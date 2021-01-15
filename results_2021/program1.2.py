x = input("Какое действие будем выполнять? ")
b = ''
if x == '^':
    n = int(input("введите число => "))
    y = int(input("В какую степень будем возводить? "))
    print("Результат =>", n**y)
elif x == '!':
    n = int(input("Введите число=> "))
    m = int(input('число бит: '))
    while n > 0:
        if m and n % 2:
            b = '0' + b
            m -= 1
        else:
            b = str(n % 2) + b
        n = n // 2
    print("Результат=>", int(b, 2))
else:
    print('Не верное действие!')