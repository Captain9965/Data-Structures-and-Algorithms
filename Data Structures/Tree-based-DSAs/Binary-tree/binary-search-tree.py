""" binary search tree Operations in python: """

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# we only use inorder traversal in this case:
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(str(root.data) + "->", end=" ")
    inorder(root.right)

#insert a node:

def insert(node, data):
    #return a new node if the tree is empty:
    if node is None:
        return Node(data)
    
    #Traverse to the right place and insert the node:
    if data < node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)
    return node

#find the inorder successor:
def minValueNode(node):
    current = node

    #find the left most leaf:
    while (current.left is not None):
        current = current.left
    return current
#deleting a node:

def deleteNode(root, data):
    if root is None:
        return root

    #find the node to be deleted:

    if data < root.data:
        root.left = deleteNode(root.left, data)
    elif data > root.data:
        root.right = deleteNode(root.right, data)

    #here we have found the key to be deleted:
    else:
        #if the node is only with one child or no child:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        #if the node has 2 children, place the inorder successor in the position of 
        #the node to be deleted:
        temp = minValueNode(root.right)
        root.key = temp.key

        #delete the inorder successor:
        root.right = deleteNode(root.right, temp.key)

    return root

if __name__ == "__main__":
 root = None
 root = insert(root, 8)
 root = insert(root, 3)
 root = insert(root, 1)
 root = insert(root, 6)
 root = insert(root, 7)
 root = insert (root, 10)
 root = insert(root, 14)
 root = insert(root, 4)

 print("Inorder traveral-> ", end = " ")
 inorder(root)

 print("\nDeleting 10: \n")
 root = deleteNode(root, 10)

 print("Inorder traveral-> ", end = " ")
 inorder(root)






    
