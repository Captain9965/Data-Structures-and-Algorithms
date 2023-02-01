/* bucket sorting in cpp: */
#include "iostream"
#include "iomanip"

using namespace std;

#define NARRAY 7
#define NBUCKET 6
#define INTERVAL 10

struct Node{
    int data;
    struct Node * next = nullptr;
};

/* function forward declarations*/

void bucketSort(int * array);
void insertionSort(struct Node * list, struct Node ** sorted);
void sortedInsert(struct Node * newNode, struct Node ** sorted);
void printArray(int * array);
void printBuckets(struct Node * list);
int getBucketIndex(int value);


/* sorting function: */
void bucketSort(int * array){
    int i, j;
    struct Node **buckets;

    /* create buckets and allocate mem size: */

    buckets = (struct Node **)malloc(sizeof(struct Node * ) * NBUCKET);

    /* initialize empty buckets: */
    for (i = 0; i < NBUCKET ; i ++){
        buckets[i] = nullptr;
    }
    /* fill the buckets with their respective elements:*/

    for (i = 0; i < NARRAY; i ++){
        struct Node * current;
        int pos = getBucketIndex(array[i]);
        current = (struct Node *)malloc(sizeof(struct Node));
        current->data = array[i];
        current->next = buckets[pos];
        buckets[pos] = current;
    }

    /* print the buckets along with their elements: */

    for ( i = 0; i < NBUCKET; i ++){
        cout << "Bucket [" << i << "] : ";
        printBuckets(buckets[i]);
        cout << endl;
    }

    /* sort the elements of each bucket: */
    struct Node * sorted;
    for ( i = 0; i < NBUCKET; ++ i){
        sorted = nullptr;
        insertionSort(buckets[i], &sorted);
        buckets[i] = sorted;

    }

    cout << "-------------------------------" << endl;
    cout << "Buckets after sorting-> "<< endl;

    for (i = 0; i < NBUCKET ; i ++){
        cout << "Bucket [" << i << "] : ";
        printBuckets(buckets[i]);
        cout << endl;      
    }

    /* insert sorted elements on array: */
    for( j = 0, i = 0; i < NBUCKET; ++i){
        struct Node * node;
        node = buckets[i];
        while (node){
            struct Node * tmp;
            array[j ++] = node->data;
            tmp = node;
            node = node->next;
            free(tmp);
        }
    }


    /* dealloacate buckets memory: */
    free(buckets);
    return;

}


/* function to sort elements in each list: */

void insertionSort(struct Node * list, struct Node ** sorted){
    Node * current = list;

    /* traverse and insert every node to sorted: */
    while (current){
        Node * next = current->next;
        sortedInsert(current, sorted);
        current = next;
    }
}

void sortedInsert(struct Node * newNode, struct Node ** sorted){

    if (!(*sorted) || (*sorted)->data >= newNode->data){
        newNode->next = (*sorted);
        (*sorted) = newNode;
        
    } else{
        Node * current = (*sorted);

        /* locate the node before point of insertion: */
        while(current->next && current->next->data < newNode->data){
            current = current->next;
        }
        newNode->next = current->next;
        current->next = newNode;
    }
}

int getBucketIndex(int value){
    return value / INTERVAL;
}



void printArray(int * array){
    for (int i = 0; i < NARRAY; ++i){
        cout << setw(3) << array[i];
    }

    cout << endl;
}

void printBuckets(struct Node *list) {
  struct Node *cur = list;
  while (cur) {
    cout << setw(3) << cur->data;
    cur = cur->next;
  }
}

int main(void) {
  int array[NARRAY] = {42, 32, 33, 52, 37, 47, 51};

  cout << "Initial array: " << endl;
  printArray(array);
  cout << "-------------" << endl;

  bucketSort(array);
  cout << "-------------" << endl;
  cout << "Sorted array: " << endl;
  printArray(array);
}