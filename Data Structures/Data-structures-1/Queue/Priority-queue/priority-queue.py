""" Priority queue application in python: """
""" heapify function:"""

def heapify(arr, n, i):
    """ find the largest among the root, left and right child:"""
    largest = i;
    l = 2 * i + 1;
    r = 2 * i + 2;

    if l < n and arr[i] < arr[l]:
        largest = l;
    if r < n and arr[r] < arr[r]:
        largest = r;

    """ swap and continue heapifying if the root is not the largest:"""
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

""" insert an element into the tree:"""
def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum)
        for i in range((size // 2 ) - 1, -1, -1):
            heapify(array, size, i)

""" delete and element:"""
def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if (num == array[i]):
            break
    array[i], array[size - 1] = array[size - 1], array[i]
    array.pop()

    for i in range((len(array) // 2 ) - 1, -1, -1):
            heapify(array, len(array), i)

if __name__ == "__main__":
    arr = []

    insert(arr, 3)
    insert(arr, 4)
    insert(arr, 9)
    insert(arr, 5)
    insert(arr, 2)

    print("\n Max heap array-> " + str(arr))
    deleteNode(arr, 4)
    print("After deleting element -> " + str(arr))
