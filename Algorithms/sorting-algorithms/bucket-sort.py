""" Bucket sort implementation in python: """
def bucketSort(array):
    bucket = []

    """ create empty buckets: """
    for i in range(len(array)):
        bucket.append([])
    
    """ insert elements into their respective buckets: """
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)
    
    """ sort the elements in each bucket: """
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])
    
    """get the sorted elements:"""
    k = 0

    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array

def printArray(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


if __name__ == "__main__":
    array = [.42, .32, .33, .52, .37, .47, .51]
    printArray(array)

    print("Array after sorting in ascending order is-> ")
    bucketSort(array)
    printArray(array)
