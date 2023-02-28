""" LCS algorithm in python: """


""" utility function to print array:"""

def printArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j], end= " ")
        print()

""" function to find LCS: """
def lcsAlgo(S1, S2, m, n):
    L = [[0 for x in range(n + 1)] for x in range(m + 1)]

    """ building the matrix from the bottom way up: """

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif S1[i - 1] == S2[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i][j - 1], L[i - 1][j])

    """index is the length of the longest common subsequence: """
    index = L[m][n]

    """print lcs array: """
    printArray(L)

    lcs = [""] * (index + 1)
    lcs[index] = ""

    i = m
    j = n 

    while i > 0 and j > 0:
        if S1[i - 1] == S2[j - 1]:
            lcs[index - 1] = S1[i - 1]
            i -= 1
            j -= 1
            index -= 1

        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    """ printing the subsequences: """

    print("S1 : " + S1 + "S2 : " + S2)
    print("LCS: " + "".join(lcs))


if __name__ == "__main__":
    S1 = "ACADB"
    S2 = "CBDA"
    m = len(S1)
    n = len(S2)
    lcsAlgo(S1, S2, m, n)