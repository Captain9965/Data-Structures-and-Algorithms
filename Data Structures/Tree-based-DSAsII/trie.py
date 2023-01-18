"""python implementation of a trie:"""

class TrieNode:
    def __init__(self):
        self.childNode = [None] * 26
        self.wordCount = 0


def insert_key(root, key):
    currentNode = root

    for i in key:
        if not currentNode.childNode[ord(i) - 97]:
            new_node = TrieNode()
            currentNode.childNode[ord(i) - 97] = new_node
        currentNode = currentNode.childNode[ord(i) - 97]
    currentNode.wordCount = currentNode.wordCount + 1

def search_key(root, key):
    currentNode = root

    for i in key:
        if  not currentNode.childNode[ord(i) - 97]:
            return False
        currentNode = currentNode.childNode[ord(i) - 97]
    return currentNode.wordCount > 0
def delete_key(root, word):
    currentNode = root
    lastBranchNode = None
    lastBranchChar = ord('a')

    for c in word:
        if not currentNode.childNode[ord(c) - 97]:
            return False
        else:
            count = 0
            for i in range(26):
                if currentNode.childNode[i]:
                    count = count + 1
            if count > 1:
                lastBranchNode = currentNode
                lastBranchChar = ord(c)
        currentNode = currentNode.childNode[ord(c) - 97]
    count = 0

    for i in range(26):
        if currentNode.childNode[i]:
            count = count + 1
    if count > 0:
        currentNode.wordCount = currentNode.wordCount - 1
        return True
    if lastBranchNode:
        lastBranchNode.childNode[lastBranchChar - 97] = None
        return True
    else:
        root.childNode[ord(word[0]) - 97] = None
        return True

if __name__ == "__main__":
    root = TrieNode()
    inputStrings = ["ant", "and", "do","geek","dad", "ball"]
    for string in inputStrings:
        insert_key(root, string)
    searchQueries = ["do", "geek", "bat"]

    for string in searchQueries:
        if(search_key(root, string)):
            print(string + " is found")
        else:
            print(string + " is not found")
    
    deleteQueries = ["geek", "tea"]

    for string in deleteQueries:
        if(delete_key(root, string)):
            print(string + " successfully deleted")
        else:
            print(string + " not found")
            