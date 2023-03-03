"""
Given a linked list, return it in reverse:
    step 1: verify constraints:
            1. What do we return if we get null or a single argument?...we return probably null or the single argument.
            

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
    def printLinkedList(self, head):
        temp = head
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

        

        loop_for = list_length
        
        for i in range(list_length - 1):            
            l = loop_for
            startNode = head
            while(l > 1):
                startNode.data, startNode.next.data = startNode.next.data, startNode.data
                startNode = startNode.next
                l -= 1
            loop_for -= 1
        return
    
    """ time is O(n)
        space complexity is O(1)
    """
    def reverse_linked_list_optimized(self):
        if self.head is None:
            return
        currentNode = self.head
        previousNode = None

        while(currentNode):
            """ first store the reference to next node:"""
            nextNode = currentNode.next
            """let next point to previous node: """
            currentNode.next = previousNode
            """ update previous node to current node:"""
            previousNode = currentNode
            """update current node to previous next node"""
            currentNode = nextNode

    """
    Given a linked list and the numbers m and n, return the linked list with only positions m to n in reverse:
        step 1: verify the constraints:
                1. Is the linked list zero indexed? It is 1 indexed.
                2. We can assume that 1 <= m <= n <= lenth of linked list

        step2: test cases:
            1. Best case test case: 1->2->3->4->5->null we will have 1->4->3->2->5 when m = 2 and n = 4
            2. 1->2->3->4->5 becomes 5->4->3->2->1 when m = 1 and n = 5
            3. 1 becomes 1 when both m and n is 1
            4. null becomes null where m an dn are zero

    """
    def reverse_sub_linked_list(self, head ,m, n):
        
        if m == n:
            return head
        if head is None:
            return None
        
        endNode = head

        """traverse to the end of the swap region: """

        l = 1

        while(l < n):
            endNode = endNode.next
            l += 1

        l = 1

        startNode = head
        prevNode = None
        while (l < m - 1):
            prevNode = startNode
            startNode = startNode.next
            l += 1

        

        l = 0
        
        self.printLinkedList(endNode)
        previousNode = endNode
        currentNode = startNode.next

        """link start node with pre-end node"""
        startNode.next = endNode




        
        # self.printLinkedList(startNode)
        # self.printLinkedList(currentNode)
        # self.printLinkedList(previousNode)

        while(l <= (n - m)):
             nextNode = currentNode.next 
             currentNode.next = previousNode
             previousNode = currentNode
             currentNode = nextNode
             l += 1
             
        return head
    
    def reverse_sub_linked_listv2(self, head,  m, n):
        if m == n:
            return head
        if head is None:
            return None
        
        position = 1
        currentNode = head
        headNode = None
        listSoFar = None
        tailNode = None
        endNode = None

        while(position <=  n + 1):
            print("looping")
            if position == m:
                # print(currentNode.data)
                endNode = currentNode
            if position == m - 1:
                print(f"Head Node: {currentNode.data}. position -> {position}")
                headNode = currentNode
                currentNode = currentNode.next
            elif position == n + 1:
                tailNode = currentNode
            elif position >= m and position <= n:
                nextNode = currentNode.next
                currentNode.next = listSoFar
                listSoFar = currentNode
                currentNode = nextNode
                # print("breaking")
            else:
                currentNode = currentNode.next

            position += 1
        self.printLinkedList(listSoFar)
        """we're done:"""
        if(endNode):
            print(f"end node -> {endNode.data}")
            endNode.next = tailNode
        if(headNode):
            headNode.next = listSoFar
        else:
            head = listSoFar
        return head
        
        
        
        



if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insertAtEnd(1)
    linked_list.insertAtEnd(2)
    linked_list.insertAtEnd(3)
    linked_list.insertAtEnd(4)
    linked_list.insertAtEnd(5)

    linked_list.printLinkedList(linked_list.head)
    ll = linked_list.reverse_sub_linked_listv2(linked_list.head, 4, 5)

    linked_list.printLinkedList(ll)
