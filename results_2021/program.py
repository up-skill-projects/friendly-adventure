def Сalculate():
    def next_Int():
        return int(input())

    def get_Operator():
        if token == "+":
            return lambda x, y: x + y
        if token == "-":
            return lambda x, y: x - y
        if token == "*":
            return lambda x, y: x * y
        if token == "/":
            return lambda x, y: x / y
        raise ValueError(f"Wrong operator: {token}")

    stack = []
    stack.append(next_Int())
    stack.append(next_Int())
    while stack[1:]:
        token = input()
        result = None
        if token.isnumeric():
            result = int(token)
        elif token in ("+", "-", "*", "/",):
            result = get_Operator()(stack.pop(), stack.pop())
        else:
            raise ValueError(f"Wrong token: {token}")
        stack.append(result)
    return stack.pop()


print(Сalculate())
