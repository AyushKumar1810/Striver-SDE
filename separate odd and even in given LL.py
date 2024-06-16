class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def split_list(head):
    odd_head = odd_tail = None
    even_head = even_tail = None

    while head:
        if head.val % 2 == 0:
            if not even_head: 
                even_head = even_tail = head# we are pointing this both pounter to the same head
            else:
                even_tail.next = head
                even_tail = even_tail.next# our head values pointing to 1st even value and we are moving our tails value 
        else:
            if not odd_head:
                odd_head = odd_tail = head
            else:
                odd_tail.next = head
                odd_tail = odd_tail.next
        head = head.next

    # Terminate the new lists
    if odd_tail:
        odd_tail.next = None
    if even_tail:
        even_tail.next = None

    return odd_head, even_head

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

odd_list, even_list = split_list(head)

print("Odd List: ", end="")
print_list(odd_list)
print("\nEven List: ", end="")
print_list(even_list)

#A demostration 
# Example Linked List
# Let's take the linked list: 1 -> 2 -> 3 -> 4 -> 5.

# Steps to Split the List
# Initialization:

# We start with the head of the list pointing to the first node.
# We initialize odd_head, odd_tail, even_head, and even_tail to None.
# Traversing the List:

# We iterate through the list using a while loop.
# Iteration 1: (Node with value 1)
# Value Check:
# 1 % 2 != 0 (1 is odd)
# Odd List:
# Since odd_head is None, we set odd_head and odd_tail to point to the current node (1).
# Iteration 2: (Node with value 2)
# Value Check:
# 2 % 2 == 0 (2 is even)
# Even List:
# Since even_head is None, we set even_head and even_tail to point to the current node (2).
# Iteration 3: (Node with value 3)
# Value Check:
# 3 % 2 != 0 (3 is odd)
# Odd List:
# odd_head is not None, so we set odd_tail.next to point to the current node (3).
# Update odd_tail to point to the current node (3).
# Iteration 4: (Node with value 4)
# Value Check:
# 4 % 2 == 0 (4 is even)
# Even List:
# even_head is not None, so we set even_tail.next to point to the current node (4).
# Update even_tail to point to the current node (4).
# Iteration 5: (Node with value 5)
# Value Check:
# 5 % 2 != 0 (5 is odd)
# Odd List:
# odd_head is not None, so we set odd_tail.next to point to the current node (5).
# Update odd_tail to point to the current node (5).
# End of List:
# The traversal is complete, and we need to terminate both lists.
# Set odd_tail.next and even_tail.next to None to mark the end of both lists.
# Resulting Lists:
# Odd List: 1 -> 3 -> 5
# Even List: 2 -> 4