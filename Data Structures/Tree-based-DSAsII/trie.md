# Trie data structure:
Used to store a collection of strings and performing efficient searches on them. Derived from reTRIEval. It follows some property that if 2 strings have the same prefix, then they have the same ancestor in the trie. It can be used to sort strings alphabetically as well as search whether a given prefix is present in the trie or not.

## Need?:

A hashtable could be used for the  same purpose(storing and retrieval) but a trie is more efficient for this. A hashtable also cannot be used for prefix-based searching.

## Advantates over a hash table:
1. Prefix-search or autocomplete can be done efficiently.
2. We can easliy print all words in alphabetical order whihc is not easy to do with hashtables.
3. No overhead of hash functions.
4. Searching for a tree amongst a large collection of strings takes place in O(L) time. It could even be less if the query string does not exist.

## Properties of a trie data structure:
1. There is one root node in each trie.
2. Each node represents a string while each edge represents a character.
3. Every node consists of an array of pointers, with each index representing a character and a flag indicating whether any string ends at the current node.
4. Can contain any number of characters including numbers, alphabets. 
5. Each path from the root to a node represents a word or a string

## Working:

Every node contains an array of pointers( 26 for a-z character words). 
So the trie is populated by filling the character array for every character present in the node. If it has already been filled, skip it.

## Basic operations in a trie data structure:
### Insertion:

1. Define a function  insert taking the root and a string we want to insert in the trie.
2. Take another pointer `currentNode` and initialize it with the root node.
3. Iterate over the length of the string and check whether the value is NULL in the pointer array at the current character of the string.
4. If NULL, make a new node and point the current character to this new node && move the curr to this new node.
5. Increment the word count of the last currNode. This implies there is a string ending currentNode.

## Searching:
Similar to insertion the only difference being that whenever we find the array of pointers in currNode does not point to the current character of the word, then return false instead of creating a new node for that character of the word.

Note that we can search for a given prefix or existance of a word in the trie.

For searching a complete word however, we have an additional check whether the word is ending at the last character or not.