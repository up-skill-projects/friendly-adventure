"""модуль"""


def fun_calcul():
    """Return the pathname of the KOS root directory."""

    def next_int():
        return int(input())

    def get_operator():
        """Return the pathname of the KOS root directory."""
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
    stack.append(next_int())
    stack.append(next_int())
    while stack[1:]:
        token = input()
        # result = None
        if token.isnumeric():
            result = int(token)
        elif token in ("+", "-", "*", "/",):
            result = get_operator()(stack.pop(), stack.pop())
        else:
            raise ValueError(f"Wrong token: {token}")
        stack.append(result)
    return stack.pop()


print(fun_calcul())
