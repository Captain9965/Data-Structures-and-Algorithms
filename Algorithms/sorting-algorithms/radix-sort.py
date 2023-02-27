""" Radix sort together with counting sort in python: """

def countingSort(array, place):
    size = len(array)
    count = [0] * 10
    output = [0] * size

    """ store the count of each element in the count array:"""
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    """ store the cumulative count: """

    for i in range(1, 10):
        count[i] += count[i - 1]

    """ find the index of each element in the original array in count array 
    and place the elements in output array:"""
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    """ copy the sorted elements into the original array:"""
    for i in range(0, size):
        array[i] = output[i]


def radixSort(array):
    """ get the maximum element: """
    max_element = max(array)
    """ Apply counting sort to sort the elements according to place value:"""
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10

def printArray(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


if __name__ == "__main__":
    data = [121, 432, 564, 23, 1, 45, 788]

    radixSort(data)
    printArray(data)