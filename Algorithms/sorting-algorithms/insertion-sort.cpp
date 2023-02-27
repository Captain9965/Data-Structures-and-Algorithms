/* cpp implementation in cpp:*/

#include "iostream"

using namespace std;

void insertionSort(int * array, ssize_t size){
    for (int i = 1; i < size ; i++){
        int key = array[i];
        int j = i - 1;

        /*compare each key with each element to the left of it until an element smaller than it is found:*/

        while(j >= 0 && key < array[j]){
            array[j + 1] = array[j];
            j--;
        }
        /*place the key after the element just smaller than it:*/

        array[j + 1] = key;
    }
}

void printArray(int * array, ssize_t size){
    for (int i = 0; i < size; i++){
        cout << array[i] <<" ";
    }
    cout << endl;
}

int main(){
    int data[] = {-2, -45, 0, 11, -9};
    ssize_t size = sizeof(data) / sizeof(data[0]);
    cout <<"Array before sorting-> " << endl;
    printArray(data, size);
    insertionSort(data, size);
    cout << "Sorted Array in ascending order-> " << endl;
    printArray(data, size);
    return 0;
}