/* huffman coding in cpp STL: */

#include "bits/stdc++.h"

using namespace std;


struct minHeapNode{
    char data;
    unsigned int freq;
    minHeapNode * left, * right;
    minHeapNode(char data, unsigned int freq){
        left = right = nullptr;
        this->data = data;
        this->freq = freq;
    }
};

/* for comparison of 2 heap nodes( needed in minHeap ):*/
struct compare{
    bool operator()(minHeapNode * left, minHeapNode* right){
        return (left->freq > right->freq);
    }
};

/* prints the huffman codes from the root of the huffman tree: */

void printCodes(struct minHeapNode * root, string str){
    if (!root){
        return;
    }

    if(root->data != '$'){
        cout << root->data << ": " << str << endl;
    }

    printCodes(root->left, str + '0');
    printCodes(root->right, str + '1');
}

void huffmanCodes(char * data, int *freq, int size){
    struct minHeapNode * left, * right, * top;

    /* create a min heap and insert all characters of data: */
    priority_queue<minHeapNode * , vector<minHeapNode * > , compare> minHeap;

    for (int i = 0; i < size; ++i){
        minHeap.push(new minHeapNode(data[i], freq[i]));
    }
    while(minHeap.size() != 1){
        left = minHeap.top();
        minHeap.pop();

        right = minHeap.top();
        minHeap.pop();

        /* '$' is a special value assigned to internal nodes, not used: */
        top = new minHeapNode('$', left->freq + right->freq);

        top->left = left;
        top->right = right;

        minHeap.push(top);
    }

    printCodes(minHeap.top(), "");
}


int main(){
    char arr[] = { 'a', 'b', 'c', 'd', 'e', 'f' };
    int freq[] = { 5, 9, 12, 13, 16, 45 };

    int size = sizeof(arr) / sizeof(* arr);
    huffmanCodes(arr, freq, size);

    return 0;
}