import sys

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def parse_expression(tokens):
    def create_tree_from_stacks():
        right = operands.pop()
        left = operands.pop()
        operator = operators.pop()
        node = TreeNode(operator)
        node.left = left
        node.right = right
        operands.append(node)

    operators = []
    operands = []

    for token in tokens:
        if token.isdigit():
            operands.append(TreeNode(int(token)))
        elif token in '+-*/':
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            # Create tree nodes until the opening parenthesis is encountered
            while operators[-1] != '(':
                create_tree_from_stacks()
            operators.pop()

    # In case the expression does not end with a closing parenthesis
    while operators:
        create_tree_from_stacks()

    return operands[-1]

def evaluate_tree(root):
    if root is None:
        return 0
    if isinstance(root.value, int):
        return root.value

    left_val = evaluate_tree(root.left)
    right_val = evaluate_tree(root.right)

    if root.value == '+':
        return left_val + right_val
    elif root.value == '-':
        return left_val - right_val
    elif root.value == '*':
        return left_val * right_val
    elif root.value == '/':
        return left_val / right_val

if __name__ == '__main__':
    expression = sys.argv[1]
    tokens = expression.split()
    root = parse_expression(tokens)
    result = evaluate_tree(root)
    print(result)
