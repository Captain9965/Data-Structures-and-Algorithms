"""
    Question:

    given an array of integers representing an elevation map, where the width of each bar
    is 1 return how much rain water can be trapped.

    step 1: verify constraints:
        1. Are the sides forming walls? No.
        2. There are no negatives.
    
    logical solution:
    Notes:
        We dont just form a container from the first values that are higher than the floor...
        The max left and right values determine the height of our container.
        We notice that the amount of water above every point is determined by the lowest wall between the 
        highest walls on either side of any point.

"""
""" Attempt one: time: O(n^2) and space: O(1)"""
def calculate_total_rain_water(array):

    total_rain_capacity = 0

    a = 0
    b = 0
    
    # find wall a:
    while(a < len(array) - 1):
        if array[a + 1] < array[a]:
            break;
        else:
            a = a + 1
    if (a >= len(array) - 2):
        return total_rain_capacity

    #lets find wall b and subsequent a values:

    while((a < len(array) - 2)):

        b = a + 2
        while(b < len(array) - 1):
            if (array[b + 1] < array[b]):
                break
            else:
                b = b + 1
                continue
        # at this point, we have found our second wall, we need to calculate conatiner capacity:
        i = a
        min_wall = min(array[a], array[b])
        while(i < b - 1):
            if ((array[i + 1]) < min_wall):
                total_rain_capacity = total_rain_capacity + (min_wall - array[i + 1])
                
            i = i + 1
        a = b
    return total_rain_capacity


""" wiser attempt:
    Time complexity -> O(n^2)
    space complexity ->O(1)


"""
def calculate_total_rain_waterV2(array):
    total_rain_capacity = 0

    for element in range(len(array)):
        max_left = 0
        max_right = 0

        """ get max left:"""
        for l in range(element):
            max_left = max(max_left, array[l])
        for r in range(len(array) - (element + 1)):
            max_right = max(max_right, array[r + element + 1])

        "get current water and add to total rain capacity: "
        element_capacity = (min(max_left, max_right) - array[element])
        if element_capacity > 0:
            total_rain_capacity = total_rain_capacity + element_capacity
    
    return total_rain_capacity



""" optimized solution:
    using 2 pointer technique to achieve a O(n) time complexity and O(1) space complexity: 

 """

def calculate_total_rain_water_optimized(array):
    total_rain_capacity = 0

    """ initialize the two pointers:"""
    pointer_left = 0
    pointer_right = len(array) - 1
    max_left = 0
    max_right = 0

    while(pointer_left < pointer_right):
        """ figure out which pointer to move  and calculate / update max_left and max_right values"""
        
        if (array[pointer_left] <= array[pointer_right]):
            """decide whether to udpdate max_left or calculate capacity:"""
            if max_left > array[pointer_left]:
                current_capacity = max_left - array[pointer_left]
                total_rain_capacity += current_capacity
            else:
                max_left = array[pointer_left]
            pointer_left += 1
        else:
            """ decide whether to update max_right or calculate capacity: """
            if max_right > array[pointer_right]:
                current_capacity = max_right - array[pointer_right]
                total_rain_capacity += current_capacity
            else:
                max_right = array[pointer_right]
            pointer_right -= 1
    return total_rain_capacity
    

if __name__ == "__main__":
    array = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
    array1 = [0, 1, 0, 3, 4, 5]
    array2 = []
    array3 = [4]
    print(calculate_total_rain_water_optimized(array))

