""" python implementation of selection sort:
    also very time inefficient, with O(n^2) time complexity in all circumstances!

"""
def selectionSort(array):
    for step in range(len(array) - 1):
        min_index = step
        for i in range(step + 1, len(array)):
            """select the minimum element in each iteration:"""
            if array[i]  < array[min_index]:
                min_index = i
        """put min at the corrent position: """
        array[step], array[min_index] =array[min_index], array[step]

if __name__ == "__main__":
    data = [-2, 45, 0, 11, -9]
    selectionSort(data)
    print('Sorted Array -> ')
    print(data)