""" Linked list implementation with all the operations in python: """

class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, new_data):
        new_node = node(new_data)
        new_node.next = self.head
        self.head = new_node
        return

    #insert after a node:
    def insertAfter(self, previous_node, new_data):
        if previous_node is None:
            print("The given previous node must be in the Linked list!")
            return
        new_node = node(new_data)
        new_node.next = previous_node.next
        previous_node.next = new_node
        return
    
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

    #delete node:
    def deleteNode(self, position):
        if self.head is None:
            return
        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return
        #find the key to be deleted:
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break
        #The key is not present:        
        if temp is None:
            return
        #Position already null
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None
        temp.next = next

    #search an element:
    def search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    #sort the Linked List:
    def sortLinkedList(self, head):
        current = head
        index = node(None)

        if head is None:
            return
        else:
            while current is not None:
                #index points to the node next to current:
                index = current.next
                while index is not None:
                    if current.data > index.data:
                        current.data, index.data = index.data, current.data
                    index = index.next
                current = current.next
    def printLinkedList(self):
        temp = self.head
        while(temp):
            print(str(temp.data), end=" ")
            temp = temp.next

if __name__ == "__main__":
    llist = LinkedList()
    llist.insertAtBeginning(2)
    llist.insertAtBeginning(4)
    llist.insertAtEnd(56)
    llist.printLinkedList()
    print(" ")
    llist.insertAfter(llist.head.next, 5)
    llist.printLinkedList()
    llist.deleteNode(3)
    print(" ")
    llist.printLinkedList()
    print(" ")
    if llist.search(4):
        print("Item found in the linked list")
    else:
        print("Item not found")

    #sorting the linked list:
    llist.sortLinkedList(llist.head)
    print(" ")
    llist.printLinkedList()