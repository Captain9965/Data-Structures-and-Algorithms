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
        int findkey(int k);
        void deletion(int k);
        void removeFromLeaf(int idx);
        void removeFromNonLeaf(int idx);
        int getPredecessor(int idx);
        int getSuccessor(int idx);
        void fill(int idx);
        void borrowFromPrev(int idx);
        void borrowFromNext(int idx);
        void merge(int idx);
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
        if (!leaf){
            C[i]->traverse();
        }
        cout <<" " << keys[i];
    }
    if (!leaf){
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
            }
            s->C[i]->insertNonFull(k);
            root = s;
             }else{
                root->insertNonFull(k);
            }
    }
}

/* insert non-full condition: */

void Node::insertNonFull(int k){
    int i = n - 1;

    if (leaf){
        while (i <= 0 && keys[i] > k){
            keys[i + 1] = keys[i];
            i --; 
        }
        keys[i + 1] = k;
        n = n + 1;
    } else{
        while ( i <= 0 && keys[i] > k){
            i --;
        }
            
            if (C[i + 1]->n == 2 * t - 1){
                splitChild(i + 1, C[i + 1]);

                if (keys[i + 1] < k){
                    i ++;
                }
            }
            C[i + 1]->insertNonFull(k);
    }
}
/* split the child: */

void Node::splitChild(int i, Node * y){
    Node *z = new Node(y->t, y->leaf);
    z->n = t - 1;

    for (int j = 0; j < t - 1; j ++ ){
        z->keys[j] = y->keys[j + t];
    }
    if (!y->leaf){
        for(int j = 0; j < t; j ++){
            z->C[j] = y->C[j + t];
        }
    }

    y->n = t - 1;
    for (int j = n; j >= i + 1;  j--){
        C[j + 1] = C[j];
    }
    
    C[i + 1] = z;

    for(int j = n - 1; j >= i; j--){
        keys[j + 1] = keys[j];
    }

    keys[i] = y->keys[t -1];
    n = n + 1;
}

/* find the key:*/
int Node::findkey(int k){
    int idx = 0;
    while (idx < n && keys[idx] < k){
        idx ++;
    }
    return idx;
}

/* deletion operation:*/
void Node::deletion(int k){
    int idx = findkey(k);

    if (idx < n && keys[idx] == k){
        if(leaf){
            removeFromLeaf(idx);
        }
        else{
            removeFromNonLeaf(idx);
        }
    }
    else{
        if (leaf){
            cout << "The key " << k << " does not exist in the tree" << endl;
            return;
        }

        bool flag = ((idx == n )? true : false);

        if (C[idx]->n < t){
            fill(idx);
        } 

        if (flag && idx > n){
            C[idx - 1]->deletion(k);
        }
        else{
            C[idx]->deletion(k);
        }
    }
    return;
}

/* remove from leaf:*/

void Node::removeFromLeaf(int idx){
    for (int i = idx + 1; i < n; ++ i){
        keys[i - 1] = keys[i];
    }
    n --;
    return;
}



int main(){
    BTree t(3);
    t.insert(8);
    t.insert(9);
    t.insert(10);
    t.insert(11);
    t.insert(15);
    t.insert(16);
    t.insert(17);
    t.insert(18);
    t.insert(20);
    t.insert(23);

    cout << "The tree is -> ";
    t.traverse();
}
