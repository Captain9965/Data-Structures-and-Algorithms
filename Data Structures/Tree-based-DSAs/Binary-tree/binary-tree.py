#binary tree application in python:

""" This is the node structure and traversal methods: """
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def traversePreorder(self):
        print(str(self.data) + "->", end=" ")

        if self.left:
            self.left.traversePreorder()
        if self.right:
            self.right.traversePreorder()
    def traversePostorder(self):
        if self.left:
            self.left.traversePostorder()
        if self.right:
            self.right.traversePostorder()
        print(str(self.data) + "->", end=" ")

    def traverseInorder(self):
        if self.left:
            self.left.traverseInorder()
        print(str(self.data) + "->", end=" ")
        if self.right:
            self.right.traverseInorder()

""" check for full binary tree: """

def isFullBtree(root):

    #1. if tree is empty:
    if root is None:
        return True
    #2. checking whether a child is present:
    if root.left is None and root.right is None:
        return True
    if root.left is not None and root.right is not None:
        return (isFullBtree(root.left) and isFullBtree(root.right))
    return False

def calculateheight(node):
    d = 0
    while (node is not None):
        d += 1
        node = node.left
    return d

def isPerfectBinaryTree(root, d, level = 0):
    #is the tree empty?
    if (root is None):
        return True
    
    #check the presence of trees:
    if (root.left is None and root.right is None):
        return (d == level + 1)

    if (root.left is None or root.right is None):
        return False
    return (isPerfectBinaryTree(root.left, d , level + 1)) and (isPerfectBinaryTree(root.right, d, level + 1))

def isCompleteBinaryTree(root, index, numberOfNodes):
    #is the tree empty?

    if root is None:
        return True
    if index >= numberOfNodes:
        return False
    return (isCompleteBinaryTree(root.left, 2 * index + 1, numberOfNodes) 
            and (isCompleteBinaryTree(root.right, 2 * index + 2, numberOfNodes)))

#do this as python does not have references:

class Height:
    def __init__(self):
        self.height = 0
        
def isHeightBalanced(root, height):
    left_height = Height()
    right_height = Height()

    if root is None:
        return True
    l = isHeightBalanced(root.left, left_height)
    r = isHeightBalanced(root.right, right_height)

    height.height = max(left_height.height, right_height.height) + 1

    if abs(left_height.height - right_height.height) <= 1:
        return l and r
    return False

    

    
def count_nodes(root):
    if root is None:
        return 0
    return (1 + count_nodes(root.left) + (count_nodes(root.right))) 


if __name__ == "__main__":
    binTree = Node(20)
    binTree.left = Node(30)
    binTree.right = Node(40)
    binTree.left.left = Node(50)
    # binTree.left.left.left = Node(70)

    print("Traversing inorder->")
    binTree.traverseInorder()
    print()

    print("Traversing preorder->")
    binTree.traversePreorder()
    print()

    print("Traversing postorder->")
    binTree.traversePostorder()
    print()

    print("Is this a full tree? -> " + ("yes" if isFullBtree(binTree) else "no"))
    print("Height of the tree:-> ", calculateheight(binTree))
    print("Is this a perfect binary tree? -> " + ("yes" if (isPerfectBinaryTree(binTree, calculateheight(binTree))) else "no"))

    nodeCount = count_nodes(binTree)
    index = 0

    print("This is the node count -> ", nodeCount)
    print()
    print("Is this a complete binary tree?-> " + ("yes" if (isCompleteBinaryTree(binTree, index, nodeCount)) else "no"))
    print()
    height = Height()
    print("Is this a balanced tree? -> " + ("yes" if (isHeightBalanced(binTree, height)) else "No"))







