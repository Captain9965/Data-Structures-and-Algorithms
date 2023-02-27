/* merge sort implementation in cpp:*/
#include "iostream"

using namespace std;

void merge(int * array, int p, int q, int r){
    /* create L -> A[p....q] and M -> A[q + 1, r] */
    int n1 = q - p + 1;
    int n2 = r - q;
    int L[n1], M[n2];

    for (int i = 0; i < n1; i ++)
        L[i] = array[p + i];
    for (int j = 0; j < n2; j ++)
        M[j] = array[q + 1 + j];
    
    /* maintain current index of sub-arrays:*/
    int i = 0, j = 0, k = p;
    /* place the elements of L and M in their correct position in A[p...r]*/

    while(i < n1 && j < n2){
        if(L[i] < M[j]){
            array[k] = L[i];
            i++;
        }else{
            array[k] = M[j];
            j++;
        }
        k++;
    }

    /* fill up the remaining elements:*/

    while (i < n1){
        array[k] = L[i];
        i++;
        k++;
    }

    while (j < n2){
        array[k] = M[j];
        j++;
        k++;
    }

}

void mergeSort(int * array, int l, int r){
    if (l < r){
        /* m is the division point*/
        int m = l + (r - l)/2;
        mergeSort(array, l, m);
        mergeSort(array, m + 1, r);

        /*merge the 2 sorted sub-arrays*/
        merge(array, l, m, r);
    }
}

void printArray(int * array, size_t size){
    for (int i = 0; i < size; i ++)
        cout << array[i] << " ";
    cout << endl;
}

int main(){
    int data[] = {-2, -45, 0, 11, -9};
    ssize_t size = sizeof(data) / sizeof(data[0]);
    cout <<"Array before sorting-> " << endl;
    printArray(data, size);
    mergeSort(data, 0, size - 1);
    cout << "Sorted Array in ascending order-> " << endl;
    printArray(data, size);
    return 0;
}