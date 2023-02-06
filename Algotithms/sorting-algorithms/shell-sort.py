""" shell sort python implementation: """

def shellSort(array, n):
    """ rearrange intervals at n/4, n/2, n/8 intervals: """
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i

            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        interval //= 2

def printArray(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

if __name__ == "__main__":
    data = [-2, 45, 0, 11, -9]
    size = len(data)

    shellSort(data, size)
    printArray(data)
