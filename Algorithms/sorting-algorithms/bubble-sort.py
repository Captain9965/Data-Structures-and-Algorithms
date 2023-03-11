""" Bubble sort python implementation (ascending order):
    * In bubble sort, we bubble up the largest number

    - Space complexity of this is O(1)
    - time complexity is O(n^2) worst case and avg case and O(n) best case
    - very inefficient and rarely used!



"""

def bubbleSort(array):
    """loop through each element in the array:"""

    for i in range(len(array)):
        swapped = False

        """ loop to compare array elements:"""
        for j in range(0, len(array) - i - 1):
            """<  in descending order:"""
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        """ No swapping means the array is already sorted:"""
        if not swapped:
            break

if __name__ == "__main__":
    data = [-2, 45, 0, 11, -9]
    bubbleSort(data)
    print('Sorted Array -> ')
    print(data)