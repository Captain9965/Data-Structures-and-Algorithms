/* selection sorting implementation in cpp(ascending order for now:)*/
#include "iostream"

using namespace std;

void swap(int & x, int & y){
    int temp = x;
    x = y;
    y = temp;
}

void selectionSort(int *array, ssize_t size){
    for(int step = 0; step < (size - 1); step++){
        int min_index = step;
        for(int i = step + 1; i < size; i++){
            /*select the minimum element in each loop and swap if there is a new minimum*/
            if (array[i] < array[min_index]){
                min_index = i;
            }
        }
        swap(array[step], array[min_index]);
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
    selectionSort(data, size);
    cout << "Sorted Array in ascending order-> " << endl;
    printArray(data, size);
    return 0;
}