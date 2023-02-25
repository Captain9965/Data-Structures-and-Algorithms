""" Question:
    You are given an array of positive integers where each integer represents 
    the height of a vertical line on a chart. Find two lines which together with 
    the x axis forms a container that would hold the greatest amount of water. Return the area of
    water it would hold.

    This is a maximal answer problem:

    questions / verify constraints:
        1. Can adjacent vertices form a container?...assumption is yes
        2. can we assume that the interval between every vertical line is one length unit?
        3. What is the minimum number of elements the array has?

    logical solution:
    
    begin with max_area as 0
    for every v:
        for every other o:
            height = v if v < o else o
            width = v - o if v > o else o - v
            area = height * width
            if area > max_area:
                max_area = area
    return max_area

Brute force solution:
Its space complexity is O(1)
Its time complexity is O(n2)

test cases:
    array1 = []
    array2 = [3]
    array = [1, 8, 6, 2, 9, 4]



we can increase its space complexity by removing the second loop:


"""

def calculate_greatest_area(array):
    max_area = 0
    for vertice in range(len(array)):
        for p2 in range(len(array) - (vertice + 1)):
            other_vertice = vertice + p2 + 1

            
            height = min(array[vertice], array[other_vertice])
            width =other_vertice - vertice

            area = width * height

            max_area = max(area, max_area)
    return max_area


"""
    Optimized solution is:
        Using the shifting two pointer method, where, from the max_area formula, 
        because we realize that if we want to maximize area,  we are to care about shifting the smaller of the 2 values of any 
        points a and b if a and b are initially maximized by placing them at the opposite ends.

        This has O(n) time complexity.
        space comlexity is O(1)

"""

def two_pointer_method(array):
    # initial max_area:
    a = 0
    b = len(array) - 1
    max_area = 0

    while (a < b):
        #update new area if greater max_area is found:
        new_area = min(array[a], array[b]) * (b - a)
        max_area = max(max_area , new_area)
        #figure out which pointer to move:
        if (array[a] <= array[b]):
            a = a + 1
        else:
            b = b - 1
    
    return max_area



if __name__ == "__main__":
    array1 = []
    array2 = [3]
    array = [1, 8, 6, 2, 9, 4]
    array3 = [7, 1, 2, 3, 9]
    print(two_pointer_method(array))
