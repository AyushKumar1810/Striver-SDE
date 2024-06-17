# Problem Statement: Given a Doubly Linked List. Delete the last of a Doubly Linked List.

# Examples
# Example 1: DLL: 1 <-> 3 <-> 4 <-> 1


# Result: DLL: 1 <-> 3 <-> 4


# Explanation: After deleting the tail node we will get a doubly linked list. The node at the end of the doubly linked list will no longer be a part of it.

# Input Format: DLL: 7 <-> 5


# Result: DLL: 7


# Explanation: 7 will be the only node left after we delete the tail node of the doubly linked list.
#NOTE: use the basic Concepts of Double LL , deleting last/tail of double LL means will go to 2nd last and we will point second_last_node.next=Null 
# Check if the list is empty. If the list is empty, there's nothing to delete.
# Traverse to the last node.
# Update the pointers:
# If the last node is the only node in the list, update the head to None.
# If there are multiple nodes, update the next pointer of the second last node to None.
class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def delete_last(self):
        if not self.head:  # If the list is empty
            return
        
        if not self.head.next:  # If there's only one node
            self.head = None
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        # Now current is the last node
        current.prev.next = None
        current.prev = None

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
dll1 = build_doubly_linked_list([1, 3, 4, 1])
dll1.print_list()  # Output: 1 <-> 3 <-> 4 <-> 1
dll1.delete_last()
dll1.print_list()  # Output: 1 <-> 3 <-> 4

dll2 = build_doubly_linked_list([7, 5])
dll2.print_list()  # Output: 7 <-> 5
dll2.delete_last()
dll2.print_list()  # Output: 7

dll3 = build_doubly_linked_list([10])
dll3.print_list()  # Output: 10
dll3.delete_last()
dll3.print_list()  # Output: (empty list)
