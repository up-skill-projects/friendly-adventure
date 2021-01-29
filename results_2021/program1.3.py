quas = input('Какое действие будем выполнять? \n1)pol-Ne_pol\n2)Ne_pol-pol\n --> ')
if quas == 'pol-Ne_pol' or "1":
    join = input("Введите Польское выражение").split()
    stack = []
    for i in join:
        if i.isdigit():
            stack.append(i)
            continue
        a = stack.pop()
        b = stack.pop()
        stack.append('({} {} {})'.format(b, i, a))
    print(stack[0])
elif quas == "Ne_pol-pol" or "2":
    """ Функция добавлявшая в стек числа и проверяющие приоритеты"""


    def rpn(s):
        lex = parse(s)
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
                        q = stack_1[0]
                        stack_1 = stack_1[1:]
                        if q == "(":
                            break
                        operand += [q]
                elif prty(stack_1[0]) < prty(ind):
                    stack_1 = [ind] + stack_1
                else:
                    while True:
                        if stack_1 == []:
                            break
                        q = stack_1[0]
                        operand += [q]
                        stack_1 = stack_1[1:]
                        if prty(q) == prty(ind):
                            break
                    stack_1 = [ind] + stack_1
            else:
                operand += [ind]
        while stack_1 != []:
            q = stack_1[0]
            operand += [q]
            stack_1 = stack_1[1:]
        return operand


    def prty(o):
        if o == "+" or o == "-":
            return 1
        elif o == "*" or o == "/":
            return 2
        elif o == "(":
            return 0


    def parse(s):
        delims = ["+", "-", "*", "/", "(", ")"]
        lex = []
        tmp = ""
        for ind in s:
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


    print(rpn(input("Введите выражение")))