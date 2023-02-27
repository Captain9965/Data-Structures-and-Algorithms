""" linear search implementation in python: """

def linearSearch(array, x):
    """ go through the array sequetially:"""

    n = len(array)
    for i in range(0, n):
        if x == array[i]:
            return i

        return False

def printArray(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

if __name__ == "__main__":
    array = [-2, 45, 0, 11, -9]
    x = -9

    if linearSearch(array, x) is not False:
        print("element {} is found".format(x))
    else:
        print("Element {} not found".format(x))