/* Quick sort algorithm in cpp:*/

#include "iostream"

using namespace std;

/* swap function:*/
void swap(int & a, int & b){
    int swap_var = a;
    a = b;
    b = swap_var;
    return;
}

/* function to print the array:*/
void printArray(int * array, ssize_t size){
    for (int i = 0; i < size; i ++){
        cout << array[i] << " ";
    }
    cout << endl;
    return;
}

/* function to rearrange the array and find the partition point: */
int partition(int * array, int low, int high){
    /* select rightmost element as pivot: */
    int pivot = array[high];
    /* pointer for greater element: */
    int i = low - 1;

    /* compare each element with the pivot: */

    for (int  j= low; j < high; j ++){
        if (array[j] <= pivot){
            /* swap this element with the pivot element pointed to by i: */
            i ++;
            swap(array[i], array[j]);
        }
    }

    /* swap pivot with greater element at i: */
    swap(array[i + 1], array[high]);

    /* return the partition point: */
    return ( i + 1 );
}

/* quicksort function: */
void quickSort(int * array, int low, int high){
    if (low < high){
        /* find the pivot elements such that elements smaller than 
        the pivot are on the left while those that are greater than 
        the pivot are on the right: */
        int pivot_point = partition(array, low, high);
        /* recursively call on the left of the pivot: */

        quickSort(array, low, pivot_point - 1);
        quickSort(array, pivot_point + 1, high);
    }
    return;
}

int main(){
    int data[] = {-2, -45, 0, 11, -9};
    ssize_t size = sizeof(data) / sizeof(*data);
    cout <<"Array before sorting-> " << endl;
    printArray(data, size);
    quickSort(data, 0, size - 1);
    cout << "Sorted Array in ascending order-> " << endl;
    printArray(data, size);
    return 0;
}

