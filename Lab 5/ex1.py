class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

def evaluate_expression(expression):
    stack = Stack()
    tokens = expression[1:-1].split()
    operator = tokens.pop(0)  # Get the first token as the operator
    if len(tokens) == 1:  # Check if it's a unary expression
        operand = int(tokens[0])
        if operator == '+':
            return operand
        elif operator == '-':
            return -operand
        else:
            return None  # Unsupported unary operator
    for token in tokens:
        if token.isdigit():
            stack.push(int(token))
        elif token in ['+', '-', '*', '/']:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.push(operand1 + operand2)
            elif token == '-':
                stack.push(operand1 - operand2)
            elif token == '*':
                stack.push(operand1 * operand2)
            elif token == '/':
                stack.push(operand1 / operand2)
    return stack.pop()

if __name__ == "__main__":
    expression = input("Enter the expression: ")
    result = evaluate_expression(expression)
    print(result)