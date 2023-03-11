"""
    given an unsorted array, return the kth largest element.
    Its the kth largest element in sorted order, not the kth distinct element.

    Divide and conquer algorithmic paradigm characteristics:
        1. multi-branched recursion
        2. Breaks problems into smaller but same sub-problems
        3. combines the solutions of the subproblems into the main solution

    verifying constraints:
    1. Assume that the answer is always possible...

"""

""" 
    Time complexity is O(n log n) -> partitioning is O(n) while this is done log n times.
    Space complexity is O(log n)

"""
def kth_largest_element(array,k):
    quickSort(array, 0, len(array) - 1)
    return array[len(array) - k]

def quickSort(array, low, high):
    if low < high:
        p = partition(array, low, high)

        quickSort(array, low, p - 1)
        quickSort(array, p + 1, high)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def kth_largest_element_quick_select(array, k):
    index_to_find = len(array) - k
    value = quickSelect(array, 0, len(array) - 1, index_to_find)
    return value

""" 
    This is Hoare's quick select that returns the partition immediately it is identified to 
    be the index of interest.

    Time complexity is O(n) as the quickselect search space is reduced by half after every call. worst case remains O(n^2) 
    as in quicksort 
    space complexity is O(l) with tail recursion

"""

def quickSelect(array, low, high, index_to_find):
    p = partition(array, low, high)
    if p == index_to_find:
        return array[index_to_find]
    elif p > index_to_find:
        return quickSelect(array, low, p - 1, index_to_find)
    else:
        return quickSelect(array, p + 1, high, index_to_find)


if __name__ == "__main__":
    testCase1 = [5, 3, 1, 6, 4, 2]
    testCase2 = [2, 3, 1, 2, 4, 2]
    testCase3 = [3]

    print(kth_largest_element_quick_select(testCase1, 5))