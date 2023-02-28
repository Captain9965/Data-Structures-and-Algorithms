/* counting sort implementation in cpp: */

#include "iostream"

using namespace std;

void printArray(int array[], int size);
void countingSort(int * array, ssize_t size){
    /* declare the output array: */
    int output[size];
    int max = array[0];

    /* find the max element: */
    for (int i = 1; i < size; i ++){
        if (array[i] > max){
            max = array[i];
        }
    }
    /* the size of the array has to be 1 more than max*/
    max ++;

    /* count array: */
    int count[max];
    /* initialize the count array with zeros: */

    for (int i = 0; i < max; i ++){
        count[i] = 0;
    }
    

    /* store the count of each element: */
    for (int i = 0; i < size; i ++){
        count[array[i]] ++;
    }

    /* store the cummulative count of each array:*/

    for (int i = 1; i < max; i ++){
        count[i] += count[i - 1];
    }
    
    /* find the index of each element of the original array in the count array
    and place the elements in the output array: */
    for (int i = size - 1; i >= 0; i--){
        output[count[array[i]] - 1] = array[i];
        count[array[i]] --;
    }

    /* copy the sorted elements into the original array:*/
    for (int i = 0; i <= size; i ++){
        array[i] = output[i];
    }
}

/*Function to print an array*/
void printArray(int array[], int size) {
  for (int i = 0; i < size; i++)
    cout << array[i] << " ";
  cout << endl;
}

/*Driver code*/
int main() {
  int array[] = {4, 2, 2, 8, 3, 3, 1};

  int n = sizeof(array) / sizeof(array[0]);
  countingSort(array, n);
  printArray(array, n);
}

