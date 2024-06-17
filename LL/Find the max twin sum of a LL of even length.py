# 2130. Maximum Twin Sum of a Linked List

# Hint:
"# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1."

# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.

# Given the head of a linked list with even length, return the maximum twin sum of the linked list.

 

# Example 1:


# Input: head = [5,4,2,1]
# Output: 6
# Explanation:
# Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
# There are no other nodes with twins in the linked list.
# Thus, the maximum twin sum of the linked list is 6. 
# Example 2:


# Input: head = [4,2,2,3]
# Output: 7
# Explanation:
# The nodes with twins present in this linked list are:
# - Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
# - Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
# Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 
# Example 3:


# Input: head = [1,100000]
# Output: 100001
# Explanation:
# There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
#NOTE : same as pallindrome concepts , first find mid , then reverse the second hald i.e after the mid then use take the "curr "pointer to the head and "twin" pointer to the mid then add them and increase the pointer "current=curr.next" and  twin=twin.next then we will return the max sum 

#NOTE: Explanation:
# Finding the middle of the linked list:

# Use the fast and slow pointer technique to locate the middle of the list. slow moves one step at a time, while fast moves two steps at a time. When fast reaches the end, slow is at the middle.
# Reversing the second half:

# Starting from the middle, reverse the second half of the list.
# Calculating twin sums:

# Pair nodes from the first half and the reversed second half, compute their sums, and track the maximum sum.
# Example Usage:
# For the input [5, 4, 2, 1]:

# The twin pairs are (5, 1) and (4, 2).
# The twin sums are 6 and 6.
# The maximum twin sum is 6.
# For the input [4, 2, 2, 3]:

# The twin pairs are (4, 3) and (2, 2).
# The twin sums are 7 and 4.
# The maximum twin sum is 7.
# For the input [1, 100000]:

# The only twin pair is (1, 100000).
# The twin sum is 100001.
# The maximum twin sum is 100001.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def pairSum(head: ListNode) -> int:
    if not head:
        return 0
    
    # Step 1: Find the middle of the linked list
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Step 2: Reverse the second half of the linked list
    prev = None
    current = slow
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    # Step 3: Calculate twin sums and find the maximum twin sum
    max_twin_sum = 0
    first_half = head
    second_half = prev
    while second_half:
        twin_sum = first_half.val + second_half.val # here in pallindrome we just see wether it's eual or not here we are adding that's only difference 
        max_twin_sum = max(max_twin_sum, twin_sum)
        first_half = first_half.next
        second_half = second_half.next
    
    return max_twin_sum

def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Test cases
head1 = build_linked_list([5, 4, 2, 1])
print(pairSum(head1))  # Output: 6

head2 = build_linked_list([4, 2, 2, 3])
print(pairSum(head2))  # Output: 7

head3 = build_linked_list([1, 100000])
print(pairSum(head3))  # Output: 100001
