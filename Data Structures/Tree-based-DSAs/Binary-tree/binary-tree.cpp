//binary tree cpp implementation:

#include "stdlib.h"
#include "iostream"

using namespace std;

struct Node {
    int data;
    struct Node * left = nullptr;
    struct Node * right = nullptr;
};

struct Node * newNode(int data){
    struct Node *node = (struct Node *)malloc(sizeof(struct Node));
    node->data = data;
    node->left = nullptr;
    node->right = nullptr;

    return node;
}

//traverse preorder:

void traversePreorder(struct Node * root){
    if (root){
        cout << root->data << " ";
        traversePreorder(root->left);
        traversePreorder(root->right);
    }
}

//traverse inorder:
void traverseInorder(struct Node * root){
    if (root){
        traverseInorder(root->left);
        cout << root->data << " ";
        traverseInorder(root->right);
    }
}

//traverse postorder:
void traversePostorder(struct Node * root){
    if (root){
        traversePostorder(root->left);
        traversePostorder(root->right);
        cout << root->data << " ";
    }
}

//checking whether the binary tree is a full binary tree:

bool isFullBinaryTree(struct Node *root){

    //is binary tree empty?
    if (!root){
        return true;
    }

    //check whether a child is present:
    if ((!root->left) && (!root->right)){
        return true;
    }

    //checking internal nodes:
    if ((root->left) && (root->right)){
        return (isFullBinaryTree(root->left) && isFullBinaryTree(root->right));
    }

    //else return false:
    return false;
}

//calculating the height of the tree:
int height(Node * root){
    int d = 0;
    while (root){
        d +=1;
        root = root->left;
    }
    return d;
}

//checking whether the binary tree is a perfect binary tree:
bool isPerfectR(Node *root, int d, int level = 0){
    //is the binary tree empty?
    if (!root){
        return true;
    }

    if (!root->left && !root->right){
        return (d == level + 1);
    }

    if (!root->left || !root->right){
        return false;
    }

    return (isPerfectR(root->left, d, level + 1 ) && (isPerfectR(root->right, d, level + 1)));
    
}
//count the number of nodes in the tree:

int countNodes(Node * root){
    if (!root){
        return 0;
    }
    return (1 + countNodes(root->left) + (countNodes(root->right)));
}

//check for a complete binary tree:
bool isCompleteBinaryTree(Node * root, int index, int nodeCount){
    if (!root){
        return true;
    }

    if (index >= nodeCount){
        return false;
    }

    return (isCompleteBinaryTree(root->left, 2 * index + 1, nodeCount) && 
            isCompleteBinaryTree(root->right, 2 * index + 2, nodeCount));
}

bool isPerfect(Node *root){
    int d = height(root);
    return isPerfectR(root, d);
}


int main(){
    struct Node * root = newNode(20);
    root->left = newNode(30);
    root->right = newNode(40);
    root->left->left = newNode(70);

    cout <<"Traverse inorder ->" << " ";
    traverseInorder(root);

    cout <<"\nTraverse preorder ->" << " ";
    traversePreorder(root);

    cout << "\nTraverse postorder ->" << " ";
    traversePostorder(root);

    cout << "\n is this a full binary tree? " << (isFullBinaryTree(root) ? "yes": "no") << " ";
    cout <<"\n is this a perfect binary tree? " << (isPerfect(root) ? "yes": "no") << " ";
    cout << "\n is this a complete binary tree? " << (isCompleteBinaryTree(root, 0, countNodes(root)) ? "yes": "no");



}
