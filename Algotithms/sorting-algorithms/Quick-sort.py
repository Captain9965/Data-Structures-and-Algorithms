""" Quick sort algorithm in python: """

def partition(array, low, high):
    """ choose the rightmost element as the pivot:"""
    pivot = array[high]
    """pointer for greater element:"""

    i = low - 1

    """ traverse through all elements comparing each with pivot.
    """
    for j in range(low, high):
        if array[j] <= pivot:
            """if element smaller than pivot is found, swap it with 
            greater element pointed to by i"""

            i = i + 1
            array[i], array[j] = array[j], array[i]
    """swap the pivot element with the greater element specified by i"""
    array[i + 1], array[high] = array[high], array[i + 1]

    """return the position from where the partition is done:"""
    return i + 1


def quickSort(array, low, high):
    if low < high:
        """find the pivot element:"""
        pi = partition(array, low, high)
        
        """recursive call on the left of the pivot:"""
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
        
def printArray(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

if __name__ == "__main__":
    data = [-2, 45, 0, 11, -9]
    size = len(data)

    quickSort(data, 0, size - 1)
    printArray(data)