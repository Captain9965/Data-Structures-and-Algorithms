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
struct Node * insertionSort(struct Node * list);
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

    for ( i = 0; i < NBUCKET; i ++){
        insertionSort(buckets[i]);

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

struct Node * insertionSort(struct Node * list){
    struct Node * k, * nodeList;
    if(!list || !list->next){
        return list;
    }

    nodeList = list; 
    k = list->next;

    nodeList->next = nullptr;

    while(k){
        struct Node * ptr;
        if(nodeList->data > k->data){
            struct Node * tmp;
            tmp = k;
            k = k->next;
            tmp->next = nodeList;
            nodeList = tmp;
            continue;
        }

        for (ptr = nodeList; ptr->next; ptr = ptr->next){
            if (ptr->next->data > k->data){
                break;
            }
        }

        if (ptr->next){
            struct Node * tmp;
            tmp = k;
            k = k->next;
            tmp->next = ptr->next;
            ptr->next = tmp;
            continue;
        } else{
            ptr->next = k;
            k = k->next;
            ptr->next->next = nullptr;
            continue;
        }

    }
    return nodeList;
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