""" counting sort in python: """

def countingSort(array):
    size = len(array)
    count = [0] * 10
    output = [0] * size

    """ store the count of each element in the count array:"""
    for i in range(0, size):
        count[array[i]] += 1

    """ store the cumulative count: """

    for i in range(1, 10):
        count[i] += count[i - 1]

    """ find the index of each element in the original array in count array 
    and place the elements in output array:"""
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    """ copy the sorted elements into the original array:"""
    for i in range(0, size):
        array[i] = output[i]
        
def printArray(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


if __name__ == "__main__":
    data = [4, 2, 2, 8, 3, 3, 1]

    countingSort(data)
    printArray(data)