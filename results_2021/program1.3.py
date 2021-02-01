"""функция расчета из обычного выражение в польское"""


def rpn(s_kas):
    lex = parse(s_kas)
    stack_1 = []
    operand = []
    opera = ["+", "-", "*", "/", "(", ")"]
    for ind in lex:
        if ind == "(":
            stack_1 = [ind] + stack_1
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
                stack_1 = [ind] + stack_1
            else:
                while True:
                    if stack_1 == []:
                        break
                    q_fst = stack_1[0]
                    operand += [q_fst]
                    stack_1 = stack_1[1:]
                    if prty(q_fst) == prty(ind):
                        break
                stack_1 = [ind] + stack_1
        else:
            operand += [ind]
    while stack_1 != []:
        q_fst = stack_1[0]
        operand += [q_fst]
        stack_1 = stack_1[1:]
    return operand


def prty(o_sr):
    if o_sr == "+" or o_sr == "-":
        return 1
    elif o_sr == "*" or o_sr == "/":
        return 2
    elif o_sr == "(":
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


"""функция расчета из польского выражения в обычное выражение"""


def funcc():
    join = input("Введите Польское выражение").split()
    stack = []
    for i in join:
        if i.isdigit():
            stack.append(i)
            continue
        a_stack = stack.pop()
        b_stack = stack.pop()
        stack.append('({} {} {})'.format(b_stack, i, a_stack))
    return stack[0]


print(rpn(input("Введите выражение")))
print(funcc())
