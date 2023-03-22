"""
    Time to inform employees question:


"""

def time_to_inform(n, headID, manager, informTime):
    graph = build_adjacency_list(n, manager)
    Maxtime = 0
    dfs(headID, graph, informTime, Maxtime)
    return Maxtime

def build_adjacency_list(n, manager):
    graph = []
    for index in range(n):
        if not graph[manager[index]]:
            graph[manager[index]] = []
        graph[manager[index]].append(index)
    return graph

def dfs(headID, graph, informTime, Maxtime):
    if not graph[headID]:
        return Maxtime
    Maxtime += informTime[headID]
    for heads in graph[headID]:
        Maxtime = max(Maxtime, dfs(heads, graph, informTime, Maxtime))
    return Maxtime

