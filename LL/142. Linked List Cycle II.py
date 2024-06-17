# 142. Linked List Cycle II
# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

# Do not modify the linked list.
# Example 1:


# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
# Example 2:


# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.
# Example 3:


# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detectCycle(head):
    if not head or not head.next:
        return None
    
    slow = fast = head
    
    # First phase: determine if there is a cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # No cycle
    
    # Second phase: find the start of the cycle
    start = head
    while start != slow:
        start = start.next
        slow = slow.next
    
    return start

# Example usage

# Creating a cycle linked list: 3 -> 2 -> 0 -> -4 -> 2 (cycle)
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Creates a cycle

cycle_start = detectCycle(node1)
print(f"Cycle starts at node with value {cycle_start.val}" if cycle_start else "No cycle")

# Creating a non-cycle linked list: 1 -> 2
node5 = ListNode(1)
node6 = ListNode(2)
node5.next = node6

cycle_start = detectCycle(node5)
print(f"Cycle starts at node with value {cycle_start.val}" if cycle_start else "No cycle")

# Creating a single node linked list: 1 (no cycle)
node7 = ListNode(1)

cycle_start = detectCycle(node7)
print(f"Cycle starts at node with value {cycle_start.val}" if cycle_start else "No cycle")



