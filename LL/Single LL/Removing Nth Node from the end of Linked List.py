class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    # Initialize two pointers
    fast = head
    slow = head
    
    # Move fast pointer n steps ahead
    for _ in range(n):
        fast = fast.next
    
    # If fast pointer reaches the end, remove the head node
    if not fast:
        return head.next
    
    # Move both pointers until fast reaches the end
    while fast.next:# we will stop fast to the tail of the LL 
        fast = fast.next
        slow = slow.next
    
    # Remove the Nth node from the end
    slow.next = slow.next.next # we will connect slow pointer next to next.next then the node at which slow pointer is there will be poiting to null that means it  has been removed, Our slow pointer will be just on one left of the Nth node from the end
    
    return head

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

# Remove 2nd node from the end: the list becomes 1 -> 2 -> 3 -> 5
new_head = removeNthFromEnd(head, 2)
print("List after removing 2nd node from the end:")
printList(new_head)
