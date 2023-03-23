"""
    determine whether it is possible to finish all courses:
    if we are using a brute force solution where we are doing bfs or dfs on all nodes, we end up 
    with a space complexity of O(n^2) and time complexity of O(n^3)


    As a result, we use topological sort...which works on directed acyclic graph..

"""

""" 
    space and time complexity:
        space -> O(n^2)
        time -> O(P + n^2)

"""
def canFinish(numCourses, prerequisites):
    adjList = [[] for i in range(numCourses)]
    inDegreeMatrix = [0 for i in range(numCourses)]
    createLists(numCourses, prerequisites, adjList, inDegreeMatrix)
    print(inDegreeMatrix, adjList)
    return not hasCycle(inDegreeMatrix, adjList)


def createLists(numCourses, prerequisites, adjList, inDegreeMatrix):
    for course in prerequisites:
        adjList[course[1]].append(course[0])
        inDegreeMatrix[course[0]] += 1

def hasCycle(inDegreeMatrix, adjList):
    stack = []
    for i in range(len(inDegreeMatrix)):
        if inDegreeMatrix[i] == 0:
            stack.append(i)
    count = 0
    while(len(stack)):
        currentNode = stack.pop()
        count += 1
        for child in adjList[currentNode]:
            inDegreeMatrix[child] -= 1
            if inDegreeMatrix[child] == 0:
                    stack.append(child)
    if count == len(inDegreeMatrix):
        return False
    else:
        return True



if __name__ == "__main__":
    prerequisites = [[1,0],[0,1]]
    prerequisites2 = [[1, 0]]
    print(canFinish(2, prerequisites2))