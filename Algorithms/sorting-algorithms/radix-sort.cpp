/* radix sort with counting sort implementation in cpp: */

#include "iostream"

using namespace std;

/* funciton declaration to print the array to std output*/
void printArray(int array[], ssize_t size);

/* get the max element in the array: */
int getMax(int * array, int size, int place){
    int max = array[0];
    for (int i = 1; i < size; i ++){
        if (((array[i] / place) % 10) > ((max / place) % 10)){
            max = array[i];
        }
    }
    return max;
}

/* using counting sort to sort the elements on the basis of significant places: */
void countingSort(int * array, ssize_t size, int place){
    /* declare the output array: */
    int output[size];

    /* find the max element: */
    int max = (getMax(array, size, place) / place) % 10;

    cout << max << endl;

    /* array size has to be 1 more than max: */
    max ++;

    /* count array optimized for the least size of array: */
    int count[max];

    /* initialize the count array with zeros: */

    for (int i = 0; i < max; i ++){
        count[i] = 0;
    }
    

    /* store the count of each element: */
    for (int i = 0; i < size; i ++){
        count[(array[i] / place) % 10] ++;
    }

    /* store the cummulative count of each array:*/

    for (int i = 1; i < max; i ++){
        count[i] += count[i - 1];
    }
    
    /* find the index of each element of the original array in the count array
    and place the elements in the output array: */
    for (int i = size - 1; i >= 0; i--){
        output[count[(array[i] / place) % 10] - 1] = array[i];
        count[(array[i] / place) % 10] --;
    }

    /* copy the sorted elements into the original array:*/
    for (int i = 0; i <= size; i ++){
        array[i] = output[i];
    }
}

/* main function to implement radix sort: */
void radixSort(int * array, ssize_t size){
    /* get max element: */
    int max = getMax(array, size, 100);
    /* apply counting sort according to place value: */

    for (int place = 1; max / place > 0; place *= 10){
        countingSort(array, size, place);
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
  int array[] = {121, 432, 564, 29, 1, 40, 700};

  int n = sizeof(array) / sizeof(array[0]);
  radixSort(array, n);
  printArray(array, n);
}

