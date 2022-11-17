""" avl tree implementation in python: """

#tree node: 

class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(object):
    def insert_node(self, root, key):
        #find the correct location and insert the node:

        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)
        
        #get the height:
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        #update the balance factor and balance the tree:
        balanceFactor = self.get_balance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        #tree is well balanced:
        return root 

    def delete_node(self, root, key):
        #find the node to be deleted and remove it:

        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValNode(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right, temp.key)
        
        if root is None:
            return root

        #get the height:
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balanceFactor = self.get_balance(root)

        #balance the tree:
        if balanceFactor > 1:
            if self.get_balance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.get_balance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root
    
    #function to perform left rotation:
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        

