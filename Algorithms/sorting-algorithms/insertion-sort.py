""" Python implementation of insertion sort(ascending order):
    useful when we know the list is almost sorted...we can easily get O(n)  complexity

"""

def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        """
        compare each key with each element to the left of it until an element smaller than it is found:
        """
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        """ place the key after the element just smaller than it:"""
        array[j + 1] = key

if __name__ == "__main__":
    data = [-2, 45, 0, 11, -9]
    insertionSort(data)
    print('Sorted Array -> ')
    print(data)