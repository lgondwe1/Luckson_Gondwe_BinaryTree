class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class OperandNode(Node):
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Operands must be numbers.")
        super().__init__(value)

class OperatorNode(Node):
    def __init__(self, operator, left, right):
        if operator not in ['+', '-', '*', '/', '^', '%']:
            raise ValueError(f"Unsupported operator: {operator}")
        super().__init__(operator, left, right)

def evaluate(node):
    if isinstance(node, OperandNode):
        return node.value

    left_value = evaluate(node.left)
    right_value = evaluate(node.right)

    if node.value == '+':
        return left_value + right_value
    elif node.value == '-':
        return left_value - right_value
    elif node.value == '*':
        return left_value * right_value
    elif node.value == '/':
        if right_value == 0:
            raise ZeroDivisionError("Division by zero is undefined.")
        return left_value / right_value
    elif node.value == '^':
        return left_value ** right_value
    elif node.value == '%':
        return left_value % right_value

# Example of a more complex tree: (7 + 3) ^ 2 % (5 - 2)
root = OperatorNode('%',
                    OperatorNode('^',
                                 OperatorNode('+', OperandNode(7), OperandNode(3)),
                                 OperandNode(2)),
                    OperatorNode('-', OperandNode(5), OperandNode(2)))

print(evaluate(root))
