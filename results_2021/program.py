def fun_calcul():
    #
    def next_int():
        # немного рекурсия по возвращению функции
        return int(input())
# Возвращение функции

    def get_operator():
        # обычные лямбда функции которые возвращают действие
        if token == "+":
            return lambda x, y: x + y
        if token == "-":
            return lambda x, y: x - y
        if token == "*":
            return lambda x, y: x * y
        if token == "/":
            return lambda x, y: x / y
        raise ValueError(f"Wrong operator: {token}")
# обычные лямбда функции которые возвращают действие
    stack = []
    stack.append(next_int())
    stack.append(next_int())
    # модуль для токенов
    while stack[1:]:
        # модуль для токенов
        token = input()
        # result = None
        if token.isnumeric():
            result = int(token)
        elif token in ("+", "-", "*", "/",):
            result = get_operator()(stack.pop(), stack.pop())
        else:
            raise ValueError(f"Wrong token: {token}")
        stack.append(result)
    # обычные лямбда функции которые возвращают действие
    return stack.pop()


print(fun_calcul())
