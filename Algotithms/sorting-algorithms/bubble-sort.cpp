/* Bubble sorting implementation in cpp(ascending order for now:)*/
#include "iostream"

using namespace std;

void swap(int & x, int & y){
    int temp = x;
    x = y;
    y = temp;
}

void bubbleSort(int *array, ssize_t size){
    /* loop to access each array element:*/
    bool swapped = false;
    for(int step = 0; step < (size - 1); step++){
        swapped = false;
        for(int i = 0; i < (size - step - 1); i++){
            /*compare 2 array elements and swap if array[i] > array[i + 1]*/
            if (array[i] > array[i + 1]){
                swap(array[i], array[i + 1]);
                swapped = true;
            }
        }
        if (!swapped){
            break;
        }
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
    bubbleSort(data, size);
    cout << "Sorted Array in ascending order-> " << endl;
    printArray(data, size);
    return 0;
}