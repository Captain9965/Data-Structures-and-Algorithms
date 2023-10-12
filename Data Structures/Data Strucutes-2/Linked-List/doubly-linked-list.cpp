#include <iostream>
#include <bits/stdc++.h>
using namespace std;
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};

class Solution {
public:
    Node* flatten(Node* head) {
        Node * curr = head;
        /* parents nodes */
        vector<Node *> parents;
        while (curr){
            if (curr->child){
                parents.push_back(curr);
            }
            curr = curr->next;
        }

        while(!parents.empty()){
            Node * parent = parents.back();
            parents.pop_back();
            Node * saved_next = parent->next;
            Node * child = parent->child;
            parent->child = nullptr;
            parent->next = child;
            child->prev = parent;
            Node * sibling = child;
            Node * last_sibling = child;

            while (sibling){
                if (sibling->child){
                    parents.push_back(sibling);
                }
                last_sibling = sibling;
                sibling = sibling->next;
            }
            if (saved_next){
                saved_next->prev = last_sibling;
                last_sibling->next = saved_next;
            }
            

        }

        return head;

    }
};