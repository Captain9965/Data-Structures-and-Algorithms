""" breadth first search in python:"""
import collections

#BFS algorithm:

def bfs(graph, root):
    visited, queue = set(), collections.deque([root])

    visited.add(root)
    while queue:
        #dequeue a vertex from the queue:
        vertex = queue.popleft()
        print(str(vertex), end=" ")

        #if not visited, mark as visited and enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

if __name__ == "__main__":
    graph = {'0': ['1', '2', '3'],
         '1': ['0', '2'],
         '2': ['0', '1', '4'],
         '3': ['0'],
         '4': ['2']}
    print("Breadth first search traversal: ->")
    bfs(graph, '0')