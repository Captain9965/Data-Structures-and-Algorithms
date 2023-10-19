#include "iostream"

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
        ListNode * hareNode = head, * tortoiseNode = head;
        while (1){
            hareNode = hareNode->next;
            tortoiseNode = tortoiseNode->next;

            if (!hareNode || !tortoiseNode){
                return nullptr;
            }
            hareNode = hareNode->next;
            if (!hareNode){
                return nullptr;
            }
            if (hareNode == tortoiseNode){
                ListNode * headNode = head, * tailNode = tortoiseNode;
                while (headNode != tailNode){
                    headNode = headNode->next;
                    tailNode = tailNode->next;
                }
                return tailNode;
            }
        }
    }
};
 
