"""
    INF represent walls, -1 represents walls and O's represent gates.
    return the array filled with the shortest distance filled in place of INF cells
    to any gate.


"""

""" 
    space and time complexity:
        space is O(n)
        time is O(n)

"""
def walls_and_gates(array):
    if len(array) == 0:
            return array
    gates = []
    for row in range(len(array)):
        for column in range(len(array[0])):
            if array[row][column] == 0:
                gates.append([row, column])
        #dfs: 
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        queue = []
        for gate in gates:
            queue.append(gate)
    while(len(queue)):
        row, column = queue.pop(0)
        new_value = array[row][column] + 1
        for direction in directions:
            new_row = row + direction[0]
            new_column = column + direction[1]
            if new_row < 0 or new_column < 0 or new_row >= len(array)\
                 or new_column >= len(array[0]) or array[new_row][new_column] == -1 or array[new_row][new_column] < new_value: 
                    continue  
            array[new_row][new_column] = new_value
            queue.append([new_row, new_column])
    return array

def print_array(array):
    for row in range(len(array)):
        for column in range(len(array[0])):
            print(array[row][column], end= " ")
        print()

if __name__ == "__main__":
    wall_array = [[float('inf'), -1, 0, -1],
                   [float('inf'), float('inf'), float('inf'), -1],
                   [float('inf'), -1, float('inf'), -1],
                   [0, -1, float('inf'), float('inf')]]
    print_array(walls_and_gates(wall_array))