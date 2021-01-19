def fun_calcul():
    """Return the pathname of the KOS root directory."""
    def next_int():
        """Return the pathname of the KOS root directory."""
        return int(input())
    """Return the pathname of the KOS root directory."""

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
    """Return the pathname of the KOS root directory."""
    stack = []
    stack.append(next_int())
    stack.append(next_int())
    """Return the pathname of the KOS root directory."""
    while stack[1:]:
        """Return the pathname of the KOS root directory."""
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
