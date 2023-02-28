""" iterative binary search in python: """


def binarySearch(array, x, low, high):
    """ repeat until pointers low and high meet each other: """
    while low <= high:
        mid = low + (high - low) // 2

        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False

if __name__ == "__main__":
    array = [3, 4, 6, 8, 90, 100]
    x = 4
    result = binarySearch(array, x, 0, len(array) - 1)
    print(result)
    if result is not False:
        print("element is found")
    else:
        print("Element not found")

