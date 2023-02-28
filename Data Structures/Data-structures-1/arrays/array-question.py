""" given an array of intergers, return the indices of the 2 numbers that sum up to a given target:

    step 1: verify the constraints:

        Ask the interviewer a number of questions:
            a. Are all the numbers positive?
            b. Are all the numbers unique or duplicates?
            c. will they always be a solution available? maybe no...there may even be an edge case where the array is empty or 
                contains only one item.
            d. what do you want to return if there is no solution? mostly null 
            e. can there be multiple numbers that add up to the value?..maybe no

    step 2: write down the test cases:

    Best case test case -> [1, 3, 7, 9, 2] -> t = 11   return -> [3, 4] 
    No solution test case -> same array  -> t = 25 -> null
                            -> [ ] t = 11 -> null
                            -> [5] t = 5 -> null because we need 2 numbers
                            -> [1, 6]  t = 7, -> [0, 1]

    step 3: Think of a working logical solution: 

    How do I approach this from a logical standpoint without any code?
    We have to think of a working solution first..

    Logically, we can easily add each number by adding each number with each other number..this is the 2 pointer technique

    step 4: write the solution in code: 
    step 5: Double check for errors
    step 6: Test solution with test cases.
    step 7: analyze the space and time complexity of the solution.
    step 8: optimizing the solution.

 

 """

 #-------------------------------------------------------------------------------------------------#
"""
    This is the brute force solution: 

    Time complexity for this algorithm is O(n2)
    space complexity for this is O(1)
"""
def returnTwoPairs(array, num):

    # if the array is empty or contains only one item, then return null or None in python
    if len(array) <= 1:
        return None
    for p1 in range(len(array)):
        for p2 in range(len(array) - (p1 + 1)):
            index1 = p1
            index2 = p1 + 1 + p2

            if (array[index1] + array[index2] == num):
                return [index1, index2]
    #if we do not find any pair, return None
    return None


"""
    we can use a hash map or a hash map like data structure to store the number we need to look for in the subsequent elements.
    This way, we do not need to use a second loop just to do the comparison:

    time complexity is -> O(n)
    space complexity is -> O(n)


"""

def hashMap_solution(array, num):
    # if the array is empty or contains only one item, then return null or None in python
    if len(array) <= 1:
        return None
        
    solutionMap = {}
    for index1 in range(len(array)):
        index2 = solutionMap.get(array[index1])
    
        if index2 is not None:
            return [index2, index1]
        else:
            solutionMap[num - array[index1]] = index1
    return None


if __name__ == "__main__":
    array = [1, 3, 7, 9, 2]
    array2 = []
    array3 = [1, 4, 34, 4, 5]
    array4 = [11]
    array5 = [9, 2]

    result = hashMap_solution(array, 11)
    if (result is not None):
        print(result)
    else:
        print("No result")

