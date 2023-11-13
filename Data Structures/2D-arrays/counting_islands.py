""" 
    count the number of islands given a 2D array:

"""

def count_islands(array):

    if not len(array):
        return 0
    # sequential traversal:
    row = 0
    column = 0
    count = 0
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    for row in range(len(array)):
        for column in range(len(array[0])):
            if array[row][column] == "1":
                count += 1
                dfs(array, row, column, directions)
    return count

"""
    space and time complexity:
        time is O(n) worst case
        space is O(n x m) worst case 

"""
def dfs(array, row, column, directions):
    if row < 0 or column < 0 or row >= len(array) or column >= len(array[0]) or array[row][column] == "0":
        return
    
    #flip to zero to avoid double counting:
    array[row][column] = "0"

    #move in all possible directions:
    for direction in directions:
        dfs(array, row + direction[0], column + direction[1], directions)

"""
    space and time complexity:
        time is O(n) worst case
        space is O(max(m, n)) worst case. has a marginal space complexity advantage over the dfs approach

"""
def bfs(array, row, column, directions):
    queue = []
    queue.append([row, column])

    while len(queue):
        row, column = queue.pop(0)
        if row < 0 or column < 0 or row >= len(array) or column >= len(array[0]) or array[row][column] == "0":
            continue
        #flip to zero to avoid double counting:
        array[row][column] = "0"

        #push to queue:
        for direction in directions:
            queue.append([row + direction[0], column + direction[1]])


if __name__ == "__main__":
    islandMatrix = [["1","1","1","1","0"],
                    ["1","1","0","1","0"],
                    ["1","1","0","0","0"],
                    ["0","0","0","0","1"]]
    print(count_islands(islandMatrix))