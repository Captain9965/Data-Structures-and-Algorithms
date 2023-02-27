#include "iostream"

using namespace std;

void swap(int * a, int * b){
    int c = * a;
    * a = * b;
    * b = c;
    return;
}

void heapify(int * array, int n, int i){

    /* find the largest index between the root and its children: */
    int largest = i;
    int l = 2 * i + 1;
    int r = 2 * i + 2;

    if ((l < n) && (array[i] < array[l])) largest = l;
    if ((r < n) &&(array[largest] < array[r])) largest = r;

    /* swap and heapify the leafif the root is not the largest for max-heap: */

    if (largest != i){
        swap(&array[i], &array[largest]);
        heapify(array, n, i);
    } 
}

void heapSort(int * array, int n){

    for (int i = n/2 - 1; i >= 0; i --){
        heapify(array, n, i);
    }

    for (int i = n - 1; i >= 0; i --){
        swap(&array[i], &array[0]);
        heapify(array, n, 0);
    }
}

void printArray(int * array, int n){
    for (int i = 0; i < n ; i ++){
        cout << array[i] << " ";
    }
    cout << endl;
}

int main(){

    int array[] = {-2, -45, 0, 11, -9};
    int size = sizeof(array)/ sizeof(* array);
    heapSort(array, size);
    printArray(array, size);
    return 0;
}