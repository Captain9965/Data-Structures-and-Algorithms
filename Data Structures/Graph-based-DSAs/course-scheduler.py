"""
    determine whether it is possible to finish all courses:
    if we are using a brute force solution where we are doing bfs or dfs on all nodes, we end up 
    with a space complexity of O(n^2) and time complexity of O(n^3)


    As a result, we use topological sort...which works on directed acyclic graph..

"""
