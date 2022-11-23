#include "iostream"

using namespace std;

typedef struct node node_t;
/* node definition: */
typedef struct node{
    int key;
    node_t* left = nullptr, * right = nullptr;
}node_t;

/* create a new node: */

node_t* newNode(int key){
    node_t* temp = (node_t* )malloc(sizeof(node_t ));
    temp->key = key;
    temp->left = temp->right = nullptr;
    return temp;
}

/* inorder traversal: */
void inorder(node_t* root){
    /* check whether root is null*/
    if (!root){
        return;
    }

    /* traverse left sub-tree:*/
    inorder(root->left);

    /* traverse root sub-tree:*/
    cout << root->key <<" ->";
    /* traverse right sub-tree*/

    inorder(root->right);

}

/* insert a node:*/

node_t* insert(node_t * node, int key){
    /* return a new node if key is empty:*/
    if(!node){
        return newNode(key);
    }

    /* traverse to the right place and insert the node:*/
    if (key < node->key){
        node->left = insert(node->left, key);
    }
    else{
        node->right = insert(node->right, key);
    }
    return node;
}

/* find the inorder successor:*/

node_t* minValNode(node_t* node){
    node_t* current = node;

    //find the left-most tree:
    while (current && current->left != nullptr){
        current = current->left;
    }
    return current;
}


/* deleting a node: */

node_t* deleteNode(node_t * root, int key){
    /* return if key is empty:*/

    if (!root){
        return root;
    }

    /* find the node to be deleted:*/
    if (key < root->key){
        root->left = deleteNode(root->left, key);
    }
    else if (key > root->key){
        root->right = deleteNode(root->right, key);
    }
    /* we  have found the node at this point: */
    else{

        /* if node has only 1 child or no child:*/
        if (!root->left){
            node_t* temp = root->right;
            free(root);
            root = nullptr;
            return temp;
        }
        else if (!root->right){
            node_t* temp = root->left;
            free(root);
            root = nullptr;
            return temp;
        }
        /* if the node has 2 children: */
        node_t* temp = minValNode(root->right);

        /* place the inorder successor in the position of the node to be deleted*/
        root->key = temp->key;

        /* delete the inorder successor: */
        root->right = deleteNode(root->right, temp->key);

    }
    return root;
}

/* driver code: */

int main(){
    node_t* root = nullptr;
    root = insert(root, 8);
    root = insert(root, 3);
    root = insert(root, 1);
    root = insert(root, 6);
    root = insert(root, 7);
    root = insert(root, 10);
    root = insert(root, 14);
    root = insert(root, 4);

    cout << " Inorder traversal: \n";
    inorder(root);

    cout << " After deleting 10: \n";
    root = deleteNode(root, 10);

    cout << " Inorder traversal: \n";
    inorder(root);


}
