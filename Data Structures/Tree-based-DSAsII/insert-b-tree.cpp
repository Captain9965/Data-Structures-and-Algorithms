/* cpp implementation of a b-tree insertion operation:*/

#include "iostream"

using namespace std;

/* node class: */
class Node{
    private:
        int *keys;
        int t;
        Node **C;
        int n;
        bool leaf;
    public:
        Node(int t , bool leaf);
        void insertNonFull(int k);
        void splitChild(int i, Node *y);
        void traverse();
        friend class BTree; 
};


/* tree class: */

class BTree{
    private:
        Node *root;
        int t;

    public:
        BTree(int _t){
            root = nullptr;
            t = _t;
        }

        void traverse(){
            if (root){
                root->traverse();
            }
        }

        void insert(int k);

};

Node::Node(int t1, bool leaf1){
    t = t1;
    leaf = leaf1;
    keys = new int[2 * t -1];
    C = new Node *[2 * t];
    n = 0;
}

/* traverse the nodes:*/

void Node::traverse(){
    int i;
    for (i = 0; i < n ; i ++){
        if (leaf == false){
            C[i]->traverse();
        }
        cout <<" " << keys[i];
    }
    if (leaf == false){
        C[i]->traverse();
    }
}

/* insert the node:*/
void BTree::insert(int k){
    if(!root){
        root = new Node(t, true);
        root->keys[0] = k;
        root->n = 1;
    }
    else{
        if(root->n == 2 * t - 1){
            Node * s = new Node(t, false);
            s->C[0] = root;
            s->splitChild(0, root);

            int i = 0;
            if (s->keys[0] < k){
                i++;
                s->C[i]->insertNonFull(k);
                root = s;
            } else{
                root->insertNonFull(k);
            }
        }
    }
}