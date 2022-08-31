"""калькулятор перевод с обычной в польскую """


def rpn(s_kas):  # модуль
    lex = parse(s_kas)
    global STACK_1
    STACK_1 = []
    operand = []
    opera = ["+", "-", "*", "/", "(", ")"]
    for ind in lex:
        if ind == "(":
            STACK_1 += [ind]
        elif ind in opera:
            if STACK_1 == []:
                STACK_1 = [ind]
            elif ind == ")":
                while True:
                    q_fst = STACK_1[0]
                    STACK_1 = STACK_1[1:]
                    if q_fst == "(":
                        break
                    operand += [q_fst]
            elif prty(STACK_1[0]) < prty(ind):
                STACK_1 += [ind]
            else:
                while True:
                    if STACK_1 == []:
                        break
                    q_fst = STACK_1[0]
                    operand += [q_fst]
                    STACK_1 = STACK_1[1:]
                    if prty(q_fst) == prty(ind):
                        break
                STACK_1 += [ind]
        else:
            operand += [ind]
    while STACK_1 != []:
        q_fst = STACK_1[0]
        operand += [q_fst]
        STACK_1 = STACK_1[1:]
    return operand


def prty(o_sr):  # модуль еслть  ли этот знак то вернуть число и добавить в стек по номеру числа
    if o_sr == "+" or "-":
        return 1
    if o_sr == "*" or "/":
        return 2
    if o_sr == "(":
        return 0


def parse(s_kas):
    delims = ["+", "-", "*", "/", "(", ")"]
    lex = []
    tmp = ""
    for ind in s_kas:
        if ind != " ":
            if ind in delims:
                if tmp != "":
                    lex += [tmp]
                lex += [ind]
                tmp = ""
            else:
                tmp += ind
    if tmp != "":
        lex += [tmp]
    return lex


def func():  # функция
    global STACK_1
    indeed = input("Введите Польское выражение").split()
    for i in indeed:
        if i.isdigit():
            STACK_1.append(i)
            continue
        d_stack = STACK_1.pop()
        r_stack = STACK_1.pop()
        STACK_1.append('({} {} {})'.format(r_stack, i, d_stack))
    return STACK_1[0]


print(rpn(input("Введите выражение")))
print(func())
