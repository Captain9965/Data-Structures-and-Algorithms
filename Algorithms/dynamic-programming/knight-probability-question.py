"""
    On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. 
    The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).

    A chess knight has eight possible moves it can make, 
    Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.

    constraints:
        1. Do we round the answer? No..


"""
"""
    space and time for this:
    O(8 ^ k) for time
    O(8 ^ k) for space 

"""
DIRECTIONS = [[-2, -1], [-2, 1], [-1, 2], [1, 2],[2, 1], [2, -1], [1, -2], [-1, -2]]
def knightsProbability(n, k, r, c):
    if r < 0 or r >= n or c < 0 or c >= n:
        return 0
    if k == 0:
        return 1
    res = 0

    for direction in DIRECTIONS:
        res += knightsProbability(n, k - 1, r + direction[0], c + direction[1]) / 8
    return res

""" 
    space complexity = O(n^2 * k)
    time is O(n^2 * k)

"""
def memoizedSolution(n, k, r, c):
    dp = [[[None for i in range(n)] for i in range(n)] for i in range(k + 1)]
    return recurse(n, k, r, c, dp)

def recurse(n, k, r, c, dp):
    if r < 0 or r >= n or c < 0 or c >= n:
        return 0
    if k == 0:
        return 1
    if dp[k][r][c] is not None:
        return dp[k][r][c]
    else:
        res = 0
        for direction in DIRECTIONS:
            res += recurse(n, k - 1, r + direction[0], c + direction[1], dp) / 8
    dp[k][r][c] = res
    return res
""""""

"""
    inital bottom up solution:
    space -> (n^2 * k)
    time -> (n^2 * k)

"""
def bottomUpSolution(n, k, r, c):
    dp = [[[0 for i in range(n)] for i in range(n)] for i in range(k + 1)]
    dp[0][r][c] = 1

    for step in range(1,k + 1):
        for row in range(n):
            for column in range(n):
                for direction in DIRECTIONS:
                    prev_row = row + direction[0]
                    prev_column = column + direction[1]
                    if prev_row >= 0 and prev_row < n and prev_column >= 0 and prev_column < n:
                        dp[step][row][column] += dp[step - 1][prev_row][prev_column] / 8

    res = 0
    for i in range(n):
        for j in range(n):
            res += dp[k][i][j]
    return res
"""
    final optimization:
    time remains the same but space reduces to O(n^2)


"""
def finalOptimization(n, k, r, c):
    prev_dp = [[0 for i in range(n)] for i in range(n)]
    current_dp = [[0 for i in range(n)] for i in range(n)]
    prev_dp[r][c] = 1

    for step in range(1,k + 1):
        for row in range(n):
            for column in range(n):
                for direction in DIRECTIONS:
                    prev_row = row + direction[0]
                    prev_column = column + direction[1]
                    if prev_row >= 0 and prev_row < n and prev_column >= 0 and prev_column < n:
                        current_dp[row][column] += prev_dp[prev_row][prev_column] / 8
        prev_dp = current_dp
        current_dp = [[0 for i in range(n)] for i in range(n)]
    res = 0
    for i in range(n):
        for j in range(n):
            res += prev_dp[i][j]
    return res


if __name__ == "__main__":
    print(finalOptimization(6, 2, 2, 2))
