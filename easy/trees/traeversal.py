

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def preorder(root):
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)

def postorder(root):
    if root:
        print(root.value)
        postorder(root.left)
        postorder(root.right)


# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Preorder traversal of binary tree is")
preorder(root)
 
print("\nInorder traversal of binary tree is")
inorder(root)
 
print("\nPostorder traversal of binary tree is")
postorder(root)