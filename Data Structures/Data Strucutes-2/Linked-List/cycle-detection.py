"""
    Answers the question: have we seen the node before??

"""

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.next = next

"""
    For this naive approach:

        Space complexity is O(n)
        Time complexity is O(n)

"""
def find_cycle(head : Node):
    if head is None:
        return None
    currentNode = head
    seenNodes = set()

    while(currentNode not in seenNodes):
        if currentNode.next is None:
            return None
        else:
            seenNodes.add(currentNode)
            currentNode = currentNode.next
    return currentNode

""" 
    Floyd and Hare's algorithm  for cycle detection: 
 
"""
def tortoise_and_hare(head: Node):
    if head is None:
        return None
    tortoiseNode = head.next
    if tortoiseNode is None:
        return None
    hareNode = head.next.next
    if hareNode is None:
        return None
    while (hareNode is not None and hareNode.next is not None):
        if(tortoiseNode == hareNode):
            tailNode = tortoiseNode
            headNode = head
            while(headNode != tailNode):
                tailNode = tailNode.next
                headNode = headNode.next
            return tailNode
        tortoiseNode = tortoiseNode.next
        hareNode = hareNode.next.next 
    return None

""" 
    Better algorithm: 

"""
def tortoise_and_hare(head: Node):
    if head is None:
        return None
    tortoiseNode = head
    hareNode = head

    while(True):
        hareNode = hareNode.next
        tortoiseNode = tortoiseNode.next

        if hareNode is None or hareNode.next is None:
            return None
        hareNode = hareNode.next
        if(tortoiseNode == hareNode):
            tailNode = tortoiseNode
            headNode = head
            while(headNode != tailNode):
                tailNode = tailNode.next
                headNode = headNode.next
            return tailNode


