"""
    Time to inform employees question:


"""
"""
    Time complexity is : O(n)
    space complexity is : O(n)


"""
def time_to_inform(n, headID, manager, informTime):
    graph = build_adjacency_list(n, manager)
    Maxtime = 0
    Maxtime = dfs(headID, graph, informTime)
    return Maxtime

def build_adjacency_list(n, manager):
    graph = [[] for i in range(n)]
    for index in range(n):
        if manager[index] != -1:
            graph[manager[index]].append(index)
    return graph

def dfs(headID, graph, informTime):
    if not graph[headID]:
        return 0
    time = 0
    for head in graph[headID]:
        time = max(time, dfs(head, graph, informTime))
    time += informTime[headID]
    return time

