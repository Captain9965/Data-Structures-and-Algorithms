#include "iostream"

using namespace std;

int linearSearch(int * array, ssize_t size, int searchItem){
    for (int i = 0; i < size; i ++){
        if (searchItem == array[i]){
            return i;
        }
    }
    return -1;
}

int main(){
    int data[] = {-2, 45, 0, 11, -9};
    int size = sizeof(data) / sizeof(* data);
    linearSearch(data, size, 90) != -1 ? cout << "Element has been found" << endl : cout << "Element has not been found" << endl;
    return 0;
}