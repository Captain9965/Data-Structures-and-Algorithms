"""
    Given a doubly linked list, list nodes have a child that points to 
    a separate doubly linked list.These child lists can also have one or more
    child doubly linked lists of their own too. Return the list as a single level flattened doubly linked list:


    verifying constraints:
        1. Change child references to null after we flatten the linked list.
    The key here is analyzing where the nodes of interest are.

"""

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

"""
    Space complexity is O(n)
    Time complexity is O(1)
"""
def flatten(self, head: Node):
    currentNode = head
    parents = []
    parentNode = None
    childHead = None
    parentRight = None
    tailNode = None

    while(currentNode):
        if currentNode.child:
            parents.append(currentNode)
        currentNode = currentNode.next
    while(len(parents) > 0):
        parentNode = parents.pop()
        childHead = parentNode.child
        currentNode = childHead
        parentNode.child = None
        while(currentNode):
            if currentNode.child:
                parents.append(currentNode)
            tailNode = currentNode
            currentNode = currentNode.next
        parentRight = parentNode.next
        parentNode.next = childHead
        childHead.prev = parentNode
        if parentRight:
            parentRight.prev = tailNode
        tailNode.next = parentRight
    return head

""" 
    Space complexity is O(1)
    Time complexity is O(n)
"""
def flatten_version2(self, head: Node):
    if head is None:
        return head
    currentNode = head
    while currentNode:
        if not currentNode.child:
            currentNode = currentNode.next
        else:
            tailNode = currentNode.child
            while tailNode.next:
                tailNode = tailNode.next
            tailNode.next = currentNode.next
            if currentNode.next:
                currentNode.next.prev = tailNode
            currentNode.next = currentNode.child
            currentNode.child.prev = currentNode
            currentNode.child = None
            currentNode = currentNode.next
    return head
            
    