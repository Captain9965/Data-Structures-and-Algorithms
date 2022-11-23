""" python implementation of insertion operation in a b-tree:"""

#node container:
class BTreeNode:
    def __int__(self, leaf = False):
        self.leaf = leaf
        self.child = []
        self.keys = []

#Tree
class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t
    #insert node:
    def insert(self, k):
        root = self.root
        if (len(root.keys) == (2 * self.t) - 1):
            temp = BTreeNode()
            self.root = temp
            temp.child.insert(0,root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

