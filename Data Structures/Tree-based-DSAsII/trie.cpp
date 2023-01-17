/* cpp implementation of the trie data structure: */

#include "bits/stdc++.h"

using namespace std;

struct TrieNode{
    /*pointer array for child nodes of each node:*/

    TrieNode * childNode[26];
    int wordCount;

    TrieNode(){
        /* constructor:*/
        wordCount = 0;
        for (int i = 0; i < 26; i ++){
            childNode[i] = nullptr;
        }
    }
};

void insert_key(TrieNode * root, string & key){
    TrieNode * currentNode = root;

    /* iterate across the length of the string:*/
    for (auto c : key){
        /* check if the node exists for the current character in the tree:*/
        if (currentNode->childNode[c - 97] == nullptr){
            /* then make a new node:*/
            TrieNode * newNode = new TrieNode();
            /* keep the reference of the newly created node:*/
            currentNode->childNode[c - 97] = newNode;
        }

        /* move the current node pointer to the newly created node:*/
        currentNode = currentNode->childNode[c - 97];
    }

    /* increment end word count fo rthe last current node to imply that 
    there is a string ending at the current node:*/
    currentNode->wordCount++;
}

bool search_key(TrieNode * root, string & key){
    TrieNode * currentNode = root;

    for (auto c : key){
        if (currentNode->childNode[c - 97] == nullptr){
            return false;
        }
        currentNode = currentNode->childNode[c - 97];
    }
    return (currentNode->wordCount > 0);
}

bool delete_key(TrieNode * root, string & word){
    TrieNode * currentNode = root;
    TrieNode * lastBranchNode = nullptr;
    char lastBranchChar = 'a';

    for (auto c : word){
        if (currentNode->childNode[c - 97] == nullptr){
            return false;
        } else{
            int count = 0;
            for (int i = 0; i < 26; i ++){
                if (currentNode->childNode[i] != nullptr) count++;
            }
            if (count > 1){
                lastBranchNode = currentNode;
                lastBranchChar = c;
            }
            currentNode = currentNode->childNode[c - 97];
        }
    }
    int count = 0;
    for (int i = 0; i < 26; i++){
        if (currentNode->childNode[i] != nullptr) count++;
    }
    /* deleted word is a prefix of other words:*/
    if (count > 0){
        currentNode->wordCount--;
        return true;
    }
    /* The deleted word shares a prefix with other words in the trie:*/
    if (lastBranchNode != nullptr){
        lastBranchNode->childNode[lastBranchChar] = nullptr;
        return true;
     }
     /* the deleted word doesn't share any common prefix with any other word in the trie:*/
     else{
        root->childNode[word[0] - 97] = nullptr;
        return true;
     }
}

int main(){
    /* make a root node:*/
    TrieNode * root = new TrieNode();
    vector< string> inputStrings = {"ant", "and", "do", "geek", "dad", "ball"};

    for (int i = 0; i < inputStrings.size(); i++){
        insert_key(root, inputStrings[i]);
    }

    vector<string> searchQueryStrings = {"do", "geek", "bat"};
    int searchQueries = searchQueryStrings.size();
 
    for (int i = 0; i < searchQueries; i++) {
        cout << "Query String : " << searchQueryStrings[i]
             << "\n";
        if (search_key(root, searchQueryStrings[i])) {
            cout << "The query string is present in the "
                    "Trie\n";
        }
        else {
            cout << "The query string is not present in "
                    "the Trie\n";
        }
    }
 
    vector<string> deleteQueryStrings = { "geek", "tea" };
 
    int deleteQueries = deleteQueryStrings.size();
 
    for (int i = 0; i < deleteQueries; i++) {
        cout << "Query String : " << deleteQueryStrings[i]
             << "\n";
        if (delete_key(root, deleteQueryStrings[i])) {
            cout << "The query string is successfully "
                    "deleted\n";
        }
        else {
            cout << "The query string is not present in "
                    "the Trie\n";
        }
    }
 
    return 0;

}