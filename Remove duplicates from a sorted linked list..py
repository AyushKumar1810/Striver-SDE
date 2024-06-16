# 83. Remove Duplicates from Sorted List
# Solved
# Easy
# Topics
# Companies
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

# Example 1:


# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:


# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
 

# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.
#NOTE: simple approach we will make a current  variable and initially it will points to head then we will use while loop , while current  and current.next is not null , then we will check condition that if current.val==current.next.val if it's then that means we have duplicate elemenet so we will break the link and we will use current.next = current.next.next , in else conditions we will just do current=current.next (we haven't found duplicate)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    if not head:
        return head
    
    current = head
    
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    
    return head

def print_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

# Helper function to create a new list node
def create_node(val):
    return ListNode(val)

# Example usage:
# Create a sample linked list: 1 -> 1 -> 2 -> 3 -> 3
head = create_node(1)
head.next = create_node(1)
head.next.next = create_node(2)
head.next.next.next = create_node(3)
head.next.next.next.next = create_node(3)

print("Original List: ", end="")
print_list(head)

result = deleteDuplicates(head)

print("\nList after removing duplicates: ", end="")
print_list(result)
