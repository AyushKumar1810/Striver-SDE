# Problem Statement: Given a doubly linked list, and a value ‘k’, insert a node having value ‘k’ at the end of the doubly linked list.

# Examples
# Example 1:

# Input Format:

# DLL: 1 <-> 2 <-> 3 <-> 4

# Value to be Inserted: 6


# Result: DLL: 1 <-> 2 <-> 3 <-> 4 <-> 6


# Explanation: A new node with value 6 has been inserted at the end of the doubly linked list after the tail node.

# Example 2:

# Input Format:

# DLL: 10 <-> 20 <-> 30

# Value to be Inserted: 40


# Result: DLL: 10 <-> 20 <-> 30 <-> 40


# Explanation: In this case, a new node with value 40 is inserted after 30 which is at the end of the doubly linked list.

#NOTE: The basic concepts of Double LL is that everynode has both next and prev value . Starting node has unique character next pointer points towards next node and previous pointer points towrds Null and the tail Pointer also have unique character Tail.prev.val will be 2nd lst node val and tail.next will be Null (dealend) That concept will be enough to solve any questions Of double LL
"#so here we have to add a node at the last , so simple right ? yes we will just go to the last and we will take temp.next=k and k.next = Null that's all ? Yes that's all "
# #Create a new node with the given value k.
# Traverse the list to find the last node.
# Update pointers:
# Set the next pointer of the last node to the new node.
# Set the previous pointer of the new node to the last node.
# Handle special cases:
# If the list is empty, the new node becomes the head of the list.
class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self, k):
        new_node = Node(k) # we will create a new node with the given value K
        if not self.head:
            self.head=new_node
            return
        current=self.head
        while current.next:# we will go to tail
            current=current.next# Till tail our current pointer will be moving
        current.next=new_node
        new_node.prev=current
    def print_list(self):
        current = self.head
        result = []
        while current:
            result.append(current.val)
            current = current.next
        print(" <-> ".join(map(str, result)))

# Test cases
dll1 = DoublyLinkedList()
dll1.insert_at_end(1)
dll1.insert_at_end(2)
dll1.insert_at_end(3)
dll1.insert_at_end(4)
dll1.insert_at_end(6)
dll1.print_list()  # Output: 1 <-> 2 <-> 3 <-> 4 <-> 6

dll2 = DoublyLinkedList()
dll2.insert_at_end(10)
dll2.insert_at_end(20)
dll2.insert_at_end(30)
dll2.insert_at_end(40)
dll2.print_list()  # Output: 10 <-> 20 <-> 30 <-> 40

