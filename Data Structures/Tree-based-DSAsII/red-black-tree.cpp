/* cpp implementation of a red-black tree: */

#include "iostream"
using namespace std;

typedef enum color{
    BLACK = 0,
    RED =1
}color_t;

struct Node{
    int data;
    Node * parent;
    Node * left;
    Node * right;
    color_t color;
};

typedef Node * NodePtr;

class RedBlackTree{
    private:
        NodePtr root;
        NodePtr TNULL;

        void intializeNULLNode(NodePtr node, NodePtr parent){
            node->data = 0;
            node->parent = parent;
            node->left = nullptr;
            node->right = nullptr;
            node->color = BLACK;
        }

        /* pre-order helper: */
        void preOrderHelper(NodePtr node){
            if (node != TNULL){
                cout << node->data << " ";
                preOrderHelper(node->left);
                preOrderHelper(node->right);
            }
        }

        void inOrderHelper(NodePtr node){
            if (node != TNULL){
                inOrderHelper(node->left);
                cout << node->data << " ";
                inOrderHelper(node->right);
            }
        }

        void postOrderHelper(NodePtr node){
            if (node != TNULL){
                postOrderHelper(node->left);
                postOrderHelper(node->right);
                cout << node->data << " ";
            }
        }

        NodePtr searchTreeHelper(NodePtr node, int key){
            if (node == TNULL || key == node->data){
                return node;
            }
            if (key < node->data){
                return searchTreeHelper(node->left, key);
            }
            return searchTreeHelper(node->right,key);
        }

        void deleteFix(NodePtr x) {
            NodePtr s;
            while (x != root && x->color == BLACK) {
                if (x == x->parent->left) {
                    s = x->parent->right;
                    if (s->color == RED) {
                    s->color = BLACK;
                    x->parent->color = RED;
                    leftRotate(x->parent);
                    s = x->parent->right;
                    }

                    if (s->left->color == BLACK && s->right->color == BLACK) {
                    s->color = RED;
                    x = x->parent;
                    } else {
                    if (s->right->color == BLACK) {
                        s->left->color = BLACK;
                        s->color = RED;
                        rightRotate(s);
                        s = x->parent->right;
                    }

                    s->color = x->parent->color;
                    x->parent->color = BLACK;
                    s->right->color = BLACK;
                    leftRotate(x->parent);
                    x = root;
                    }
                } else {
                    s = x->parent->left;
                    if (s->color == RED) {
                    s->color = BLACK;
                    x->parent->color = RED;
                    rightRotate(x->parent);
                    s = x->parent->left;
                    }

                    if (s->right->color == BLACK && s->right->color == BLACK) {
                    s->color = RED;
                    x = x->parent;
                    } else {
                    if (s->left->color == BLACK) {
                        s->right->color = BLACK;
                        s->color = RED;
                        leftRotate(s);
                        s = x->parent->left;
                    }

                    s->color = x->parent->color;
                    x->parent->color = BLACK;
                    s->left->color = BLACK;
                    rightRotate(x->parent);
                    x = root;
                    }
                  }
                }
            x->color = BLACK;
            }
        void rbTransplant(NodePtr u, NodePtr v){
            if (u->parent == nullptr){
                root = v;
            } else if (u == u->parent->left) {
                u->parent->left = v;
            } else{
                u->parent->right = v;
            }
            v->parent = u->parent;
        }

        void deleteNodeHelper(NodePtr node, int key){
            NodePtr z = TNULL;
            NodePtr x, y;
            while (node != TNULL) {
                if (node->data == key) {
                    z = node;
                }

                if (node->data <= key) {
                    node = node->right;
                } else {
                    node = node->left;
                }
            }

            if (z == TNULL) {
                cout << "Key not found in the tree" << endl;
                return;
            }

            y = z;
            int y_original_color = y->color;
            if (z->left == TNULL) {
                x = z->right;
                rbTransplant(z, z->right);
            } else if (z->right == TNULL) {
                x = z->left;
                rbTransplant(z, z->left);
            } else {
                y = minimum(z->right);
                y_original_color = y->color;
                x = y->right;
                if (y->parent == z) {
                    x->parent = y;
                } else {
                    rbTransplant(y, y->right);
                    y->right = z->right;
                    y->right->parent = y;
                }

                rbTransplant(z, y);
                y->left = z->left;
                y->left->parent = y;
                y->color = z->color;
            }
            delete z;
            if (y_original_color == BLACK) {
                deleteFix(x);
            }
        }

        void insertFix(NodePtr k) {
            NodePtr u;
            while (k->parent->color == RED) {
                if (k->parent == k->parent->parent->right) {
                    u = k->parent->parent->left;
                    if (u->color == RED) {
                        u->color = BLACK;
                        k->parent->color = BLACK;
                        k->parent->parent->color = RED;
                        k = k->parent->parent;
                    } else {
                    if (k == k->parent->left) {
                        k = k->parent;
                        rightRotate(k);
                    }
                    k->parent->color = BLACK;
                    k->parent->parent->color = RED;
                    leftRotate(k->parent->parent);
                    }
                } else {
                    u = k->parent->parent->right;

                    if (u->color == RED) {
                    u->color = BLACK;
                    k->parent->color = BLACK;
                    k->parent->parent->color = RED;
                    k = k->parent->parent;
                    } else {
                    if (k == k->parent->right) {
                        k = k->parent;
                        leftRotate(k);
                    }
                    k->parent->color = BLACK;
                    k->parent->parent->color = RED;
                    rightRotate(k->parent->parent);
                    }
                }
                if (k == root) {
                    break;
                }
            }
            root->color = BLACK;
        }

        void printHelper(NodePtr root, string indent, bool last) {
            if (root != TNULL) {
                cout << indent;
                if (last) {
                    cout << "R----";
                    indent += "   ";
                } else {
                    cout << "L----";
                    indent += "|  ";
                }

                string sColor = root->color ? "RED" : "BLACK";
                cout << root->data << "(" << sColor << ")" << endl;
                printHelper(root->left, indent, false);
                printHelper(root->right, indent, true);
            }
        }
        


        
};