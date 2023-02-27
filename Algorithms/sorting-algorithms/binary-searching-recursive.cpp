/* binary searching recursive algorithm */
#include "iostream"

using namespace std;

int binarySearch(int * array, int searchItem, int low, int high){
    if (low <= high){
        int mid = low + (high - low) / 2;

        if (array[mid] == searchItem){
            return mid;
        } else if(array[mid] < searchItem){
            return binarySearch(array, searchItem, mid + 1, high);
        } else{
            return binarySearch(array, searchItem, low, mid - 1);
        }
    }
    return -1;
}

int main(){
    int sortedArray[] = {2, 4, 5, 7, 8, 9, 20};
    int searchItem = 2;
    ssize_t size = sizeof(sortedArray) / sizeof(* sortedArray);
    int result = binarySearch(sortedArray, searchItem, 0, size - 1 );
    if (result != -1){
        cout << "Item has been found with index " << result << endl;
    } else{
        cout << "Item not found" << endl;
    }
    return 0;
}