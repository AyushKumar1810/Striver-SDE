# 328. Odd Even Linked List
# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
# Example 2:


# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]
 

# Constraints:

# The number of nodes in the linked list is in the range [0, 104].
# -106 <= Node.val <= 106
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head):
    if not head or not head.next:
        return head
    
    odd = head
    even = head.next
    even_head = even
    
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    
    odd.next = even_head
    
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
# Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
head = create_node(1)
head.next = create_node(2)
head.next.next = create_node(3)
head.next.next.next = create_node(4)
head.next.next.next.next = create_node(5)

print("Original List: ", end="")
print_list(head)

result = oddEvenList(head)

print("\nReordered List: ", end="")
print_list(result)
