"""
    Question: 
    Write a function that given any 9 * 9 sudoky puzzle, gives the solution: 

"""
import math
""" 
    Thinking from the brute force approach...
    time complexity is O((n!)^n) where n is 9
    space complexity is O(1) It is a 9 by 9 board

"""
def solveSudoku(board: list):
    n = len(board)
    rows = [set() for i in range(n)]
    columns = [set() for i in range(n)]
    boxes = [set() for i in range(n)]

    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] != ".":
                value = board[r][c]
                boxId = getBoxId(r, c)
                boxes[boxId].add(value)
                rows[r].add(value)
                columns[c].add(value)
    solveBacktrack(board, boxes, rows, columns, 0, 0)

def solveBacktrack(board, boxes, rows, columns, r, c):
    if r >= len(board) or c >= len(board[0]):
        return True
    if board[r][c] == ".":
        for i in range(1,10):
            numVal = str(i)
            board[r][c] = numVal
            boxId = getBoxId(r, c)
            box = boxes[boxId]
            row = rows[r]
            column = columns[c]
            if isValid(box, row, column, numVal):
                box.add(numVal)
                row.add(numVal)
                column.add(numVal)
                if c == len(board[0]) - 1:
                    if solveBacktrack(board, boxes, rows, columns, r + 1, 0):
                        return True
                else:
                    if solveBacktrack(board, boxes, rows, columns, r, c + 1):
                        return True
                box.remove(numVal)
                column.remove(numVal)
                row.remove(numVal)
        board[r][c] = "."
    else:
        if c == len(board[0]) - 1:
            if solveBacktrack(board, boxes, rows, columns, r + 1, 0):
                return True
        else:
            if solveBacktrack(board, boxes, rows, columns, r, c + 1):
                return True
    return False
            
def isValid(box, row, column, num):
    return not (num in box or num in column or num in row)


def getBoxId(row, column):
    columnVal = math.floor(column /3)
    rowVal = math.floor(row / 3) * 3
    return rowVal + columnVal

if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    solveSudoku(board)
    print(board)