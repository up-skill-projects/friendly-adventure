"""калькулятор перевод с польской в обычную """

join = input("Введите Польское выражение").split()
stack = []
polskiu = []
for i in join:
    if i.isdigit():
        stack.append(i)
        continue
    a_stack = stack.pop()
    b_stack = stack.pop()
    stack.append('({} {} {})'.format(b_stack, i, a_stack))
print(stack[0])


def resalt():  # калькулятор
    for xin in join:
        if xin == '+':
            g_pop = polskiu.pop()
            z_pop = polskiu.pop()
            polskiu.append(g_pop + z_pop)
        elif xin == '-':
            g_pop = polskiu.pop()
            z_pop = polskiu.pop()
            polskiu.append(z_pop - g_pop)
        elif xin == '*':
            g_pop = polskiu.pop()
            z_pop = polskiu.pop()
            polskiu.append(g_pop * z_pop)
        elif xin == '^':
            g_pop = polskiu.pop()
            z_pop = polskiu.pop()
            polskiu.append(g_pop ** z_pop)
        elif xin == '/':
            g_pop = polskiu.pop()
            z_pop = polskiu.pop()
            polskiu.append(z_pop // g_pop)
        else:
            polskiu.append(int(xin))
    return polskiu[0]


print(resalt())
