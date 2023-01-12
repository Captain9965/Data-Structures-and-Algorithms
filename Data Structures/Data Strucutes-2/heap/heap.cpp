/* Max heap data structure in cpp:*/
#include "iostream"
#include "bits/stdc++.h"

using namespace std;

/*swap function*/
void swap(int *a, int *b){
    int temp = *b;
    *b = *a;
    *a = temp;
}

/* heapify function: */
void heapify(vector<int> &h, int i){
    int size = h.size();
    int largest = i;

    int l = 2 * i + 1;
    int r = 2 * i + 2;

    if (l < size && h[l] < h[largest]){
        largest = l;
    }
    if(r < size && h[r] < h[largest]){
        largest = r;
    }

    if (largest != i){
        swap(&h[i], &h[largest]);
        heapify(h, largest);
    }
}
/*insert function: */
void insert(vector<int> &h, int NewNum){
    int size = h.size();
    if(size == 0) h.push_back(NewNum);
    else{
        h.push_back(NewNum);
        for(int i = size / 2 - 1 ; i >= 0; i --) heapify(h, i);
    }
}

/* void deleteNode:*/

void deleteNode(vector<int> &h, int num){
    int size = h.size();
    int i;
    for(int i = 0; i < size; i ++)if (h[i] == num)break;
    
    swap(&h[i], &h[size - 1]);
    h.pop_back();

    for (int i = size/2 - 1; i >= 0; i --) heapify(h, i);

}

/* print array:*/
void printArray(vector<int> &h){
    for (int i = 0; i < h.size() ; i ++){
        cout << h[i] << " ";
    }
    cout << endl;
}

/* driver code:*/

int main(){
    vector<int> heapTree;

    /* insert elements:*/
    insert(heapTree, 3);
    insert(heapTree, 4);
    insert(heapTree, 9);
    insert(heapTree, 5);
    insert(heapTree, 2);

    cout << "Max heap array-> \n";
    printArray(heapTree);
    deleteNode(heapTree, 4);
    cout <<"\n After deleting 4: "<< endl;
    printArray(heapTree);
}



