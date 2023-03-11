""" Merge sort in python:
    Space complexity is O(n) due to recursion
    Time complexity is O(n log n ) hence very perfomant
"""

def mergeSort(array):
    if len(array) > 1:
        """r is the division point of the 2 sub-arrays"""
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        """sort the 2 halves:"""
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0
        """ until we reach the end of either L and M,pick the 
        larger element among elements L and M and place them in the correct position at A[p...r]"""
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1


        """ when we run out of elements in either L or M, we pick up the remaining elements and 
        put in A[p...r]"""
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
        
def printArray(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

if __name__ == "__main__":
    data = [-2, 45, 0, 11, -9]
    mergeSort(data)
    printArray(data)