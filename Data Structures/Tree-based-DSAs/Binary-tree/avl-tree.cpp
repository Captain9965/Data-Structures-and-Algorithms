/**
 * @file avl-tree.cpp
 * @author Lenny Orengo
 * @brief avl tree cpp implementation
 * @version 0.1
 * @date 2022-11-21
 */
#include "iostream"

using namespace std;

/* avl tree class: */
class Node{
    public:
        int key;
        Node * left;
        Node * right;
        int height;
};

/* max num math helper:*/
int max(int a, int b){
    return (a > b )? a : b;
}

/* get height: */

int height(Node * n){
    if (!n){
        return 0;
    }
    return n->height;
}

/*new node creation */
Node * newNode(int key){
    Node * node = new Node();
    node->key = key;
    node->left = nullptr;
    node->right = nullptr;
    node->height = 1;
    return node;
}

/* right rotate: */

Node * rightRotate(Node * y){
    Node * x = y->left;
    Node * T2 = x->right;
    x->right = y;
    y->left = T2;
    y->height = max(height(y->left), height(y->right)) + 1;
    x->height = max(height(x->left), height(x->right)) + 1;
    return x;
}

/* rotate left: */

Node * leftRotate(Node * x){
    Node * y = x->right;
    Node * T3 = y->left;
    y->left = x;
    x->right = T3;
    y->height = max(height(y->left), height(y->right)) + 1;
    x->height = max(height(x->left), height(x->right)) + 1;
    return y;
}

/* get balance factor of each node:*/

int getBalanceFactor(Node * n){
    if(!n){
        return 0;
    }
    return height(n->left) - height(n->right);

}

/* insert node */

Node * insertNode(Node * node, int key){
    /* find the correct pos and insert the node:*/

    if (!node){
        return newNode(key);
    }

    if (key < node->key){
        node->left = insertNode(node->left, key);
    }
    else if (key > node->key){
        node->right = insertNode(node->right, key);
    }
    return node;
    /* update the balance factore of each node and balance the tree:*/
    node->height = 1 + max(height(node->left), height(node->right));

    int balanceFactor = getBalanceFactor(node);
    if (balanceFactor > 1){
        if (key < node->left->key){
            return rightRotate(node);
        }
        else if (key > node->left->key){
            node->left = leftRotate(node);
            return rightRotate(node);
        }
    }
    if (balanceFactor < -1){
        if (key > node->right->key){
            return leftRotate(node);
        }
        else if (key < node->right->key){
            node->right = rightRotate(node->right);
            return leftRotate(node);
        }
    }
    return node;

}
/* node with minimum value:*/

Node * nodeWithMinVal(Node * node){
    Node * current = node;
    while (current->left){
        current = current->left;
    }
    return current;
}

/* deleting a node:*/

Node * deleteNode(Node * root, int key){
    /* find the node and delete it:*/

    if (!root){
        return root;
    }
    if (key < root->key){
        root->left = deleteNode(root->left, key);
    }
    else if (key > root->key){
        root->right = deleteNode(root->right, key);
    }
    else{
        if (!root->left || !root->right){
            Node * temp = root->left ? root->left : root->right;
            if (!temp){
                temp = root;
                root = nullptr;
            } else{
                *root = *temp;
                free(temp);
            }
        } else{
            Node * temp = nodeWithMinVal(root->right);
            root->key = temp->key;
            root->right = deleteNode(root->right, temp->key);
        }
    }

    if (!root){
        return root;
    }

    /* update the balance factor of each node and balance the tree:*/
    
}