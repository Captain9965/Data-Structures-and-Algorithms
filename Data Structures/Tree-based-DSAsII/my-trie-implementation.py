""" implement a trie with the following methods: 
    Trie() Initializes the trie object.
    void insert(String word) Inserts the string word into the trie.
    boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

"""
class LetterNode:
    def __init__(self, end = False):
        self.isEnd = end
        self.children = dict()
    def end(self):
        self.isEnd = True
    def isEndNode(self):
        return self.isEnd

"""
     complexity is O(L) for time
    for space it is O(N) because of storing every value

"""
class Trie:

    def __init__(self):
        self.root = LetterNode()
        
    def insert(self, word: str) -> None:
        currentNode = self.root
        for i in range(len(word)):
            if not currentNode.children.get(word[i]):
                currentNode.children[word[i]] = LetterNode()
            currentNode = currentNode.children.get(word[i])
        currentNode.end()
            
    def search(self, word: str) -> bool: 
        currentNode = self.root
        for i in range(len(word)):
            if not currentNode.children.get(word[i]):
                return False
            currentNode = currentNode.children.get(word[i])
        return currentNode.isEndNode()
    
    def startsWith(self, prefix: str) -> bool:
        currentNode = self.root
        for i in range(len(prefix)):
            if not currentNode.children.get(prefix[i]):
                return False
            currentNode = currentNode.children.get(prefix[i])
        return True