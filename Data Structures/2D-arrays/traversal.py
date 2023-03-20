""" bfs in 2-d arrays: """
def bfs(array):
    for row in range(len(array)):
        for column in range(len(array[row])):
            print(array[row][column], end= " ")
        print()

""" dfs in 2-d arrays:"""

def dfs(array, visited = {} , row = 0, column = 0):
    if not visited.get(row):
        visited[row] = {column}
    else:
        if column not in visited.get(row):
            visited.get(row).add(column)
        else:
            return
    
    print(array[row][column])

    if row > 1:
        dfs(array, visited, row - 1, column)
    if column < len(array[0]) - 1:
        dfs (array, visited,row, column + 1)
    if row < len(array) - 1:
        dfs (array, visited, row + 1, column)
    if column > 1:
        dfs(array, visited, row, column - 1)


"""
    space complexity is O(n)
    time complexity is O(n)
"""

def dfs_v2(array):
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    visited = [[False for y in range(len(array[0]))] for x in range(len(array))]
    values = []
    dfs_traverse(array,values, visited, directions)
    return values

def dfs_traverse(array, values, visited, directions, row = 0, column = 0):
    if row < 0 or column < 0 or row >= len(array) or column >= len(array[0]) or visited[row][column]:
        return
    
    visited[row][column] = True   
    values.append(array[row][column])
    for direction in directions:
        dfs_traverse(array, values,visited, directions, row + (direction[0]), column + direction[1])

def bfs_traverse(array,row = 0, column = 0):
    visited = [[False for y in range(len(array[0]))] for x in range(len(array))]
    if not len(array):
        return []
    queue = []
    values = []
    queue.append((row, column))
    values.append(array[row][column])
    bfs(array, values, visited, queue)
    return values

def bfs(array, values, visited, queue):
    if not len(queue):
        return
    row, column = queue.pop(0)
    if row > 1:
        if not visited[row - 1][column]:
            queue.append((row - 1, column))
            visited[row - 1][column] = True
            values.append(array[row - 1][column])
    if column < len(array[0]) - 1:
        if not visited[row][column + 1]:
            queue.append((row, column + 1))
            visited[row][column + 1] = True
            values.append(array[row][column + 1])
    if row < len(array) - 1:
        if not visited[row + 1][column]:
            queue.append((row + 1, column))
            visited[row + 1][column] = True
            values.append(array[row + 1][column])
    if column > 1:
        if not visited[row][column - 1]:
            queue.append((row, column - 1))
            visited[row][column - 1] = True
            values.append(array[row][column - 1])
    bfs(array, values, visited, queue)

"""
    space complexity is O(n)
    time complexity is O(n)

"""
def bfs_v2(array,row = 0, column = 0):
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    visited = [[False for y in range(len(array[0]))] for x in range(len(array))]
    if not len(array):
        return []
    queue = []
    values = []
    queue.append((row, column))
    while (len(queue)):
        row, column = queue.pop(0)
        if row < 0 or column < 0 or row >= len(array) or column >= len(array[0]) or visited[row][column]:
            continue
        visited[row][column] = True
        values.append(array[row][column])

        for direction in directions:
            queue.append((row + direction[0], column + direction[1]))

    return values
        

if __name__ == "__main__":

    array = [
        [0, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11,12],
        [13, 14, 15, 16, 17, 18]
    ]

    print(bfs_v2(array),)

    
