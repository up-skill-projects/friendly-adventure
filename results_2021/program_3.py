# функция расчета из обычного выражение в польское


def rpn(s_kas):  # модуль
    lex = parse(s_kas)
    global stack_1
    stack_1 = []
    operand = []
    opera = ["+", "-", "*", "/", "(", ")"]
    for ind in lex:
        if ind == "(":
            stack_1 += [ind]
        elif ind in opera:
            if stack_1 == []:
                stack_1 = [ind]
            elif ind == ")":
                while True:
                    q_fst = stack_1[0]
                    stack_1 = stack_1[1:]
                    if q_fst == "(":
                        break
                    operand += [q_fst]
            elif prty(stack_1[0]) < prty(ind):
                stack_1 += [ind]
            else:
                while True:
                    if stack_1 == []:
                        break
                    q_fst = stack_1[0]
                    operand += [q_fst]
                    stack_1 = stack_1[1:]
                    if prty(q_fst) == prty(ind):
                        break
                stack_1 += [ind]
        else:
            operand += [ind]
    while stack_1 != []:
        q_fst = stack_1[0]
        operand += [q_fst]
        stack_1 = stack_1[1:]
    return operand


def prty(o_sr):  # модуль
    if o_sr == "+" or o_sr == "-":
        return 1
    if o_sr == "*" or o_sr == "/":
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
    indeed = input("Введите Польское выражение").split()
    for i in indeed:
        if i.isdigit():
            stack_1.append(i)
            continue
        d_stack = stack_1.pop()
        r_stack = stack_1.pop()
        stack_1.append('({} {} {})'.format(r_stack, i, d_stack))
    return stack_1[0]


print(rpn(input("Введите выражение")))
print(func())
