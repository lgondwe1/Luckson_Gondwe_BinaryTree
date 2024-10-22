class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

root = Node('*')
root.left = Node('+')
root.right = Node('-')
root.left.left = Node(7)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(2)

def evaluate(node):
    if isinstance(node.value, int):
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
        return left_value / right_value

print(evaluate(root))