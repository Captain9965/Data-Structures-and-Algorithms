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

 

 """

def returnTwoPairs(array):
    for p1 in range(len(array)):
        for p2 in range(len(array) - (p1 + 1)):
            print(array[p1], end= " ")
            print(array[p1 + 1 + p2])


if __name__ == "__main__":
    array = [1, 3, 7, 9, 2]
    returnTwoPairs(array)