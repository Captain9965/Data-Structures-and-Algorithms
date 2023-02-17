""" recursive binary search in python: """

def binarySearch(array, x, low, high):
    if low <= high:
        mid = low + (high - low) // 2
        """if found at the mid, then return it: """

        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binarySearch(array, x, low, mid - 1)
        else:
            return binarySearch(array, x,  mid + 1, high)
    else:
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