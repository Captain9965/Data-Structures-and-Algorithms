#include "iostream"
using namespace std;

void shellSort(int * array, int n){
    for ( int interval = n /2 ; interval > 0; interval /= 2){
        for (int i = interval; i < n; i++){
            int temp = array[i];
            int j;
            for (j = i; j >= interval && array[j - interval] > temp; j -= interval){
                array[j] = array[j - interval];

            }
            array[j] = temp;
        }
    }
}

void printArray(int * array, ssize_t size){
    for (int i = 0; i < size; i++){
        cout << array[i] << " ";
    }   
    cout << endl;
}


int main(){
    int data[] = {-2, 45, 0, 11, -9};
    int size = sizeof(data) / sizeof(* data);
    shellSort(data, size);
    printArray(data, size);
}