"""DFS implementation in python: """

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in [x for x in graph[start] if x not in visited]:
        dfs(graph, next, visited)
    return visited

if __name__ == "__main__":
    graph = {'0': ['1', '2', '3'],
         '1': ['0', '2'],
         '2': ['0', '1', '4'],
         '3': ['0'],
         '4': ['2']}

    print(dfs(graph, '0'))