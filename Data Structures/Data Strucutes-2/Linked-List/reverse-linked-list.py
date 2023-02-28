"""
Given a linked list, return it in reverse:
    step 1: verify constraints:
            1. What do we return if we get null or a single argument?...we return probably null or the single argument.
            2. 

"""


class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    #insert at the end:
    def insertAtEnd(self, new_data):
        new_node = node(new_data)
        #traverse to the end:
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node
        return
    def printLinkedList(self):
        temp = self.head
        while(temp):
            print(str(temp.data), end="->")
            temp = temp.next
        print()

    def reverse_linked_list(self, head: node):
        if head is None:
            return
        currentNode = head
        list_length = 0
        while(currentNode):
            list_length += 1
            currentNode = currentNode.next
        print(list_length)

        l = list_length
        startNode = head
        
        for i in range(list_length - 1):
            print(startNode.data)
            while(l > 1):
                startNode.data, startNode.next.data = startNode.next.data, startNode.data
                startNode = startNode.next
                l -= 1
        return

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insertAtEnd(1)
    linked_list.insertAtEnd(2)
    linked_list.insertAtEnd(3)
    linked_list.insertAtEnd(4)
    linked_list.insertAtEnd(5)

    linked_list.printLinkedList()
    linked_list.reverse_linked_list(linked_list.head)
    linked_list.printLinkedList()
