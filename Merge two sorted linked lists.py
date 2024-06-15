# 21. Merge Two Sorted Lists uisng extra space
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    # Initialize a dummy node to form the new sorted list
    dummy = ListNode()
    current = dummy
    
    # Traverse both lists
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # If one of the lists is not exhausted, append the remaining nodes
    if list1:
        current.next = list1
    elif list2:
        current.next = list2
    
    # Return the head of the merged list
    return dummy.next

# Helper function to create a linked list from a list of values
def createLinkedList(arr):
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print the linked list
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Example usage
# List1: 1 -> 2 -> 4
list1 = createLinkedList([1, 2, 4])
# List2: 1 -> 3 -> 4
list2 = createLinkedList([1, 3, 4])

# Merging the lists
mergedList = mergeTwoLists(list1, list2)

# Printing the merged list
printList(mergedList)  # Output should be 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None
