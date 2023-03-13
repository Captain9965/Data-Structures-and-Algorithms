"""

    Given an array of intergers sorted in ascending order, return the start and end indices of a given target 
    value in an array ie. [x, y]...this should run in O(log n) time:
    verify constraints: 
        1. No found value? -> return -1



"""

"""
    this runs in O(n) time since we are moving element by element once we found the mid.

"""
def start_and_end_index_linear_search(array, low, high, k):
    if low <= high:
        mid = (low + high) // 2
        if array[mid] == k:
            left = mid
            right = mid
            while(left > 0):
                if array[left - 1] == k:
                    left -= 1
                else:
                    break
            while(right < len(array) - 1):
                if array[right + 1] == k:
                    right += 1
                else:
                    break
            return [left, right]
        elif array[mid] < k:
            return start_and_end_index_linear_search(array, mid + 1, high, k)
        else:
            return start_and_end_index_linear_search(array, low, mid - 1, k)
    else:
        return [-1, -1]

""" 
    using binary search instead for O(log n) time:


"""
def start_and_end_index_bin_search(array, low, high, k):
    if low <= high:
        mid = (low + high) // 2
        if array[mid] == k:
            return mid
        elif array[mid] < k:
            return start_and_end_index_bin_search(array, mid + 1, high, k)
        else:
            return start_and_end_index_bin_search(array, low, mid - 1, k)
    else:
        return -1


def searchRange(array, target):
    mid = start_and_end_index_bin_search(array, 0, len(array) - 1, target)
    if mid == -1:
        return [-1, -1]
    else:
        left = mid
        right = mid
    

if __name__ == "__main__":
    testCase1 = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7]
    testCase2 = []
    print(searchRange(testCase2, 5))