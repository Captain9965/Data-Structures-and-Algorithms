""" avl tree implementation in python: """
import sys
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
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    #right rotation:
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    #get the height of the node:
    def getHeight(self, root):
        if not root:
            return 0
        return root.height
    #get balance factor of the node:
    def get_balance(self, root):
        if not root:
            return 0
        return (self.getHeight(root.left) - self.getHeight(root.right))
    #def getMinValNode:
    def getMinValNode(self, root):
        if root.left is None or root.right is None:
            return root
        return self.getMinValNode(root.left)

    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.key), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)
    
    #print helper:
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R---")
                indent +="   "
            else:
                sys.stdout.write("L---")
                indent+="|   "
            print(currPtr.key)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)

if __name__ == "__main__":
    myTree = AVLTree()

    root = None

    nums = [33, 13, 52, 9, 21, 61, 8, 11]

    #populate the tree:
    for num in nums:
        root = myTree.insert_node(root, num)
    myTree.printHelper(root, "", True)

    key = 61
    root = myTree.delete_node(root, key)

    print("After deletion: ")

    myTree.printHelper(root, "", True)
    



        
