# Reverse a Doubly Linked List

# Problem Statement: Given a doubly linked list of size ‘N’ consisting of positive integers, your task is to reverse it and return the head of the modified doubly linked list.

# Examples
# Example 1:

# Input Format:

# DLL: 1 <-> 2 <-> 3 <-> 4


# Result: DLL: 4 <-> 3 <-> 2 <-> 1


# Explanation: The doubly linked list is reversed and its last node is returned at the new head pointer.

# Example 2:

# Input Format:

# DLL: 10 <-> 20 <-> 30


# Result: DLL: 30 <-> 20 <-> 10


# Explanation: In this case, the doubly linked list is reversed and its former tail is returned as its new head.
class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def reverse_list(self):
        if not self.head or not self.head.next:  # If list is empty or has only one node
            return self.head
        
        current = self.head
        previous = None
        
        while current:
            next_node = current.next  # Save the next node
            current.next = previous  # Reverse the current node's next pointer , "next will be points towards prev in reverse LL"
            current.prev = next_node  # Reverse the current node's prev pointer , "prev will points towards next in reverse LL"
            previous = current  # Move previous to the current node , "updating the pointer"
            current = next_node  # Move to the next node , "updating the Pointer"
       
        self.head = previous  # Update the head to the last processed node (originally the tail)
        return self.head

    def print_list(self):
        current = self.head
        result = []
        while current:
            result.append(current.val)
            current = current.next
        print(" <-> ".join(map(str, result)))

def build_doubly_linked_list(values):
    if not values:
        return None
    
    dll = DoublyLinkedList()
    dll.head = Node(values[0])
    current = dll.head
    
    for value in values[1:]:
        new_node = Node(value)
        current.next = new_node
        new_node.prev = current
        current = new_node
    
    return dll

# Test cases
dll1 = build_doubly_linked_list([1, 2, 3, 4])
dll1.print_list()  # Output: 1 <-> 2 <-> 3 <-> 4
dll1.reverse_list()
dll1.print_list()  # Output: 4 <-> 3 <-> 2 <-> 1

dll2 = build_doubly_linked_list([10, 20, 30])
dll2.print_list()  # Output: 10 <-> 20 <-> 30
dll2.reverse_list()
dll2.print_list()  # Output: 30 <-> 20 <-> 10
