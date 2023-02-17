""" Floyd warshall algorithm in python: """

INF = 999

def floydWarshall(G, nV):
    distance = list(map(lambda i : list(map(lambda j : j, i)), G))
    """ adding vertices individually: """
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    printSolution(distance, nV)

def printSolution(distance, nV):
    for i in range(nV):
        for j in range(nV):
            if (distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end= " ")
        print(" ")

if __name__ == "__main__":
    G = [[0, 3, INF, 5],
         [2, 0, INF, 4],
         [INF, 1, 0, INF],
         [INF, INF, 2, 0]]
    print(len(G[0]))
    floydWarshall(G, len(G[0]))