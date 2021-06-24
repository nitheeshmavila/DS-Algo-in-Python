
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def inorder(root):
    current = root
    stack = []
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.value)
            current = current.right
        else:
            break


def preorder(root):
    current = root
    stack = []
    while True:
        if current is None and len(stack) == 0:
            break

        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            print(current.value)
            current = current.right

# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

 
print("\nInorder traversal of binary tree is")
inorder(root)