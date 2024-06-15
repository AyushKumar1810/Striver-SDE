# 876. Middle of the Linked List

# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# Example 2:


# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

# Constraints:

# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100

#NOTE: simple only use of slow and fast pointers : We will tke two pointers fast and slow initia;;y Both are at head position , fast will be 2X ahead of slow , fast = fast.next.next . then we will use while Loop till fast and slow not equal to null till fast reaches it's end the slow will be at the middle , In simple way if someone is running at speed of 2times the 1st then defineltly he will complete the race and the 1st one will be in the middle of the race . it is optimised one as we have completed it in with single Go 
#NOTE: we cann also go for 1.5Go if we find the length and the we easily find the mid node of LL

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

# Example usage
# Creating the linked list [1, 2, 3, 4, 5]
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Finding the middle node
middle = middleNode(head)

# Collecting the values from the middle to the end to verify the output
result = []
while middle:
    result.append(middle.val)
    middle = middle.next

print(result)  # Output should be [3, 4, 5]

# Creating the linked list [1, 2, 3, 4, 5, 6]
head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))

# Finding the middle node
middle2 = middleNode(head2)

# Collecting the values from the middle to the end to verify the output
result2 = []
while middle2:
    result2.append(middle2.val)
    middle2 = middle2.next

print(result2)  # Output should be [4, 5, 6]


