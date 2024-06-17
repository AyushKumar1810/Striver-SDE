# 206. Reverse Linked List

# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
 

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

#NOTE:Iterative Approach  , In this we will create two pointers prev and current , prev will point to null and current will be at head (initially) then after starting of while lopp we will swap prev with current and current with current.next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    prev = None
    current = head
    while current:
        next_node = current.next  # Save the next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev one step forward
        current = next_node       # Move current one step forward
    return prev  # New head of the reversed list
#Recursive Approach

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseListRecursive(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    p = reverseListRecursive(head.next)
    head.next.next = head
    head.next = None
    return p
def printList(head: ListNode):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Helper function to create a linked list from a list
def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Example 1
head1 = createLinkedList([1, 2, 3, 4, 5])
print("Original List:")
printList(head1)

reversed_head1_iter = reverseList(head1)
print("Reversed List (Iterative):")
printList(reversed_head1_iter)

head2 = createLinkedList([1, 2, 3, 4, 5])
reversed_head2_rec = reverseListRecursive(head2)
print("Reversed List (Recursive):")
printList(reversed_head2_rec)

# Example 2
head3 = createLinkedList([1, 2])
print("Original List:")
printList(head3)

reversed_head3_iter = reverseList(head3)
print("Reversed List (Iterative):")
printList(reversed_head3_iter)

head4 = createLinkedList([1, 2])
reversed_head4_rec = reverseListRecursive(head4)
print("Reversed List (Recursive):")
printList(reversed_head4_rec)

# Example 3
head5 = createLinkedList([])
print("Original List:")
printList(head5)

reversed_head5_iter = reverseList(head5)
print("Reversed List (Iterative):")
printList(reversed_head5_iter)

reversed_head5_rec = reverseListRecursive(head5)
print("Reversed List (Recursive):")
printList(reversed_head5_rec)
