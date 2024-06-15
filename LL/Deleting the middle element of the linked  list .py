# 2095. Delete the Middle Node of a Linked List
# Hint
# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
 

# Example 1:


# Input: head = [1,3,4,7,1,2,6]
# Output: [1,3,4,1,2,6]
# Explanation:
# The above figure represents the given linked list. The indices of the nodes are written below.
# Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
# We return the new list after removing this node. 
# Example 2:


# Input: head = [1,2,3,4]
# Output: [1,2,4]
# Explanation:
# The above figure represents the given linked list.
# For n = 4, node 2 with value 3 is the middle node, which is marked in red.
# Example 3:


# Input: head = [2,1]
# Output: [2]
# Explanation:
# The above figure represents the given linked list.
# For n = 2, node 1 with value 1 is the middle node, which is marked in red.
# Node 0 with value 2 is the only node remaining after removing node 1.
#NOTE: simple only use of slow and fast pointers : We will tke two pointers fast and slow initialy Both are at head position , fast will be 2X ahead of slow ,fast = fast.next.next . then we will use while Loop till fast and slow not equal to null till fast reaches it's end the slow will be at the middle then we will shift the pointer of slow,next to slow.next.next then we will return the LL In simple way if someone is running at speed of 2times the 1st then defineltly he will complete the race and the 1st one will be in the middle of the race . it is optimised one as we have completed it in with single Go 
#NOTE: we cann also go for 1.5Go if we find the length and the we easily find the mid node of LL
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Base Case Checking 
        if head is not None or head.next is not None:
            return None
        
        slow , fast = head , head.next.next 
         # Two-Pointer Approach to Find the Middle Node
        while fast and fast.next:
            slow= slow.next
            fast=fast.next  
        # Delete the Middle Node
        slow.next = slow.next.next
        # Return the Updated Head
        return head
