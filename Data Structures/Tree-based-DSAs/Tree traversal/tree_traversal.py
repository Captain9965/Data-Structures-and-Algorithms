""" Tree traversal in python: """

class Node:
    def __init__(self,item):
        self.left = None
        self.right = None
        self.data = item
    
def inorder(root):
    if root:
        inorder(root.left)
        #traverse root:
        print(str(root.data) + "->", end=" ")
        #traverse right:
        inorder(root.right)
def postorder(root):
    if root:
        inorder(root.left)
        #traverse right:
        inorder(root.right)
        print(str(root.data) + "->", end=" ")

def preorder(root):
    if root:
        print(str(root.data) + "->", end=" ")
        #traverse left:
        inorder(root.left)
        #traverse right:
        inorder(root.right)

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(5)
    root.left.right = Node(90)

    print("**********inorder traversal***************")
    inorder(root)
    print()
    print("**********postorder traversal*****************")
    postorder(root)
    print()
    print("**********preorder traversal*****************")
    preorder(root)