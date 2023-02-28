"""Heap sort implementation in python: """ 


def heapSort(array):
    n = len(array)

    """ build max heap: """

    for i in range(n//2, -1, -1):
        heapify(array, n, i)
    
    for i in range(n - 1, 0, -1):

        """ swap: """
        array[i], array[0] = array[0], array[i]


        """ heapify root element: """
        heapify(array, i, 0)

def heapify(array, n, i):

    """ find the largest among the root and its children: """
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[i] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r

    """ if root is not the largest, swap with the root and continue heapifying: """
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)

def printArray(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


if __name__ == "__main__":
    data = [-2, -45, 0, 11, -9]
    heapSort(data)
    printArray(data)