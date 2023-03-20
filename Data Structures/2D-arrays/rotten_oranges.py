"""
  with 2 representing a bad orange, and 1 a good orange. Find out how many minutes it would take for the entire bunch to be 
  rotten
  verify constraints:
    1. If none of them will rot, return -1

    
    time and space analysis-> 
        time is O(n)
        space is O(n)

"""

def orangesRotting(array):
        if len(array) == 0:
            return 0
        good_oranges = 0
        rotting_centers = []
        for row in range(len(array)):
            for column in range(len(array[0])):
                if array[row][column] == 1:
                    good_oranges += 1
                elif array[row][column] == 2:
                    rotting_centers.append([row, column])
        #dfs: 
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        queue = []
        for oranges in rotting_centers:
            queue.append(oranges)

        initial_length = len(queue)
        processed_items = 0
        minutes = 0
        while len(queue):
            if initial_length == 0:
                minutes += 1
                initial_length = len(queue)
            row, column = queue.pop(0)
            initial_length -= 1
            for direction in directions:
                new_row = row + direction[0]
                new_column = column + direction[1]
                if new_row < 0 or new_column < 0 or new_row >= len(array)\
                 or new_column >= len(array[0]) or array[new_row] [new_column] != 1:
                    continue  
                good_oranges -= 1
                array[new_row][new_column] = 2
                queue.append([new_row, new_column])

        
        if good_oranges > 0:
            return - 1
        else:
            return minutes



