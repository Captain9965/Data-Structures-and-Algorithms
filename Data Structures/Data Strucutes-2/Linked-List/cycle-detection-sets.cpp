#include "iostream"
#include "bits/stdc++.h"
using namespace std;


/*Definition for singly-linked list. */

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
  };
 
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if (!head){
            return nullptr;
        }
        set <ListNode *> nodes;
        ListNode * current = head;
        while (nodes.find(current) == nodes.end()){
            if (!current->next){
                return nullptr;
            } else {
                nodes.insert(current);
                current = current->next;
            }
        }
        return current;
    }
};