# Tree traversal:

Unlike linear data structures which have only one way to do this, trees have several methods.
We can traversed trees by considering a tree as a node carrying data and two sub-trees.

Since the goal is to visit every node, we should visit every node in the left sub-tree, visit the node and visit the right sub-tree.

Depending on order, there can be 3 ways of doing this:

1. inorder traversal:
    
    left->root->right
2. preorder traversal:

    root->left->right
3. postorder traversal:

    left->right->root

To do the actual traversal, the nodes can be pushed on to a stack, or this could be done through recursion. 
