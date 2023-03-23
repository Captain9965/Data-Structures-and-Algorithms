"""
    determine whether it is possible to finish all courses:
    if we are using a brute force solution where we are doing bfs or dfs on all nodes, we end up 
    with a space complexity of O(n^2) and time complexity of O(n^3)


    As a result, we use topological sort...which works on directed acyclic graph..

"""
def canFinish(numCourses, prerequisites):
    adjList = [[] for i in range(numCourses)]
    inDegreeMatrix = [0 for i in range(numCourses)]
    createLists(numCourses, prerequisites, adjList, inDegreeMatrix)
    return not hasCycle(inDegreeMatrix, adjList)


def createLists(numCourses, prerequisites, adjList, inDegreeMatrix):
    for course in prerequisites:
        adjList[course[1]].append(course[0])
        inDegreeMatrix[course[0]] += 1

def hasCycle(inDegreeMatrix, adjList):
    seen = []
    currentNode = None
    while 1:
        for i in range(len(inDegreeMatrix)):
            if inDegreeMatrix[i] == 0 and i not in seen:
                currentNode = i
                break;
        if currentNode is None:
            break;
        seen.append(currentNode)
        for child in adjList[currentNode]:
            inDegreeMatrix[child] -= 1
    if len(seen) == len(inDegreeMatrix):
        return True
    else:
        return False



if __name__ == "__main__":
    prerequisites = [[1,0],[0,1]]
    canFinish(len(prerequisites), prerequisites)