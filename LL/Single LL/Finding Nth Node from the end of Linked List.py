# #NOTE: [Only head is given] return mode;(LeetCode)
# 19. Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

#NOTE: very simple approach we could simply find the length Of given LL and the we can search Nth elements from the starting using formula m-n+1 (m is length of LL) 

#NOTE : The optimised way is to take two pointer fast and slow , imitially Noth will be at head then after fast will move nth node ahead of slow and till when fast will reach Null(end of the LL) Then the slow pinter will be pointing to the Nth node from the last of LL
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findNthFromEnd(head, n):
    fast = head
    slow = head
    
    # Move the fast pointer n steps ahead
    for _ in range(n):
        if not fast:
            return None  # In case n is larger than the list length
        fast = fast.next
    
    # Move both pointers until the fast pointer reaches the end of the list
    while fast:
        fast = fast.next
        slow = slow.next
    
    return slow  # The slow pointer is now at the Nth node from the end

# Helper function to print the linked list
def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Example Usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original list:")
printList(head)

# Find the 2nd node from the end
nth_node = findNthFromEnd(head, 2)
if nth_node:
    print(f"Nth node from the end: {nth_node.val}")
else:
    print("List has fewer nodes than n.")


# Example Usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original list:")
printList(head)
# Remove 2nd node from the end: the list becomes 1 -> 2 -> 3 -> 5
new_head = findNthFromEnd(head, 2)
print("List after removing 2nd node from the end:")
printList(new_head)
