def compute(expression):
    stack = []
    tokens = expression.split()

    def apply_operator(op, a, b):
        if op == '+': return a + b
        elif op == '-': return a - b
        elif op == '*': return a * b
        elif op == '/': return a / b

    for token in reversed(tokens):
        if token.isdigit(): 
            stack.append(int(token))
        elif token in '+-*/':  
            if len(stack) < 2:
                raise ValueError("Invalid expression: not enough operands for the operator.")
            operand_a = stack.pop()
            operand_b = stack.pop()
            result = apply_operator(token, operand_a, operand_b)  
            stack.append(result)
        else:
            raise ValueError(f"Invalid token: {token}")

    if len(stack) != 1:
        raise ValueError("Invalid expression: final stack size is not 1.")
    return stack.pop()

if __name__ == '__main__':
    user_input = input("Enter an expression: ")
    expr = user_input.replace('(', '').replace(')', '')
    try:
        result = compute(expr)
        print(f"Result: {result}")
    except ValueError as e:
        print(e)