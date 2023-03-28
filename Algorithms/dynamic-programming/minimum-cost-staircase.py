"""
Question:

    You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
    Once you pay the cost, you can either climb one or two steps.
    You can either start from the step with index 0, or the step with index 1.
    Return the minimum cost to reach the top of the floor.

"""
"""
    time is O(n) because we are doubling our search space
    space complexity is O(n)

    This is a top down approach: 
"""

def minCostClimbingStairs(cost: list):
    n = len(cost)
    dp = [None for i in range(n)]

    return min(minCost(cost, n - 1, dp), minCost(cost, n - 2, dp))

def minCost(cost: list, i, dp: list):
    if i < 0:
        return 0
    if i == 0 or i == 1:
        return cost[i]
    if dp[i] is not None:
        return dp[i]
    dp[i] = cost[i] + min(minCost(cost, i - 1, dp), minCost(cost, i - 2, dp))
    return dp[i]

"""
    This further reduces the space complexity to O(1)

"""
def minCostBottomUp(cost: list):
    n = len(cost)
    last_step = cost[1]
    second_last_step = cost[0]
    for i in range(2, n):
            currentVal = cost[i] + min(last_step, second_last_step)
            second_last_step = last_step
            last_step = currentVal
    return min(last_step, second_last_step)

if __name__ == "__main__":
    cost = [20, 15, 30]
    print(minCostBottomUp(cost))
