# 234. Palindrome Linked List
# Given the head of a singly linked list, return true if it is a 
# palindrome
#  or false otherwise.
# Example 1:
# Input: head = [1,2,2,1]
# Output: true
# Example 2:
# Input: head = [1,2]# Output: false
# Constraints:
# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
" # Follow up: Could you do it in O(n) time and O(1) space?"
#NOTE:Finding the middle:

# Use two pointers, slow and fast. Move slow by one step and fast by two steps. When fast reaches the end, slow will be at the middle.
# Reversing the second half:

# Starting from the middle, reverse the second half of the list.
# Comparing both halves:

# Compare the nodes of the first half with the nodes of the reversed second half.
# Restoring the list (optional):

# This step is optional. If you need to restore the list to its original state, you can reverse the second half again and reconnect it.
# This approach ensures that you only traverse the list a few times, achieving O(n) time complexity and using O(1) extra space.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: ListNode) -> bool:
    if not head or not head.next:
        return True
    # Step 1: Find the middle of the linked list
    slow =fast = head
    while fast and fast.next:
        slow = slow.next
        fast=fast.next.next
    # Step 2: Reverse the second half of the linked list
    prev = None
    current = slow
    while current:
        next_node=current.next
        current.next=prev
        prev = current
        current=next_node
  # Step 3: Compare the first half with the reversed second half
    first_half = head
    second_half = prev
    while second_half:
        if first_half.val!=second_half.val:
            return False
        first_half=first_half.next
        second_half=second_half.next
    return True

def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)

# Test cases
head1 = build_linked_list([1, 2, 2, 1])
print(isPalindrome(head1))  # Output: True

head2 = build_linked_list([1, 2])
print(isPalindrome(head2))  # Output: False


