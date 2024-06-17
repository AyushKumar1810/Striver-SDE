# 138. Copy List with Random Pointer

# Hint
"# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null."

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.

 

# Example 1:


# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Example 2:


# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
# Example 3:



# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList(head: 'Node') -> 'Node':
    if not head:
        return None
    
    # Step 1: Create new nodes and insert them between the original nodes
    current = head
    while current:
        new_node = Node(current.val, current.next)
        current.next = new_node
        current = new_node.next
    
    # Step 2: Assign random pointers for the new nodes
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next
    
    # Step 3: Separate the original and copied lists
    original = head
    copy = head.next
    new_head = head.next
    
    while original:
        original.next = original.next.next
        if copy.next:
            copy.next = copy.next.next
        original = original.next
        copy = copy.next
    
    return new_head

# Helper function to build a linked list with random pointers from a list
def build_linked_list(arr):
    if not arr:
        return None
    nodes = [Node(val) for val, _ in arr]
    for i, (val, random_index) in enumerate(arr):
        if i < len(arr) - 1:
            nodes[i].next = nodes[i + 1]
        if random_index is not None:
            nodes[i].random = nodes[random_index]
    return nodes[0]

# Helper function to print the list to verify deep copy
def print_linked_list(head):
    result = []
    current = head
    while current:
        random_index = None
        if current.random:
            random_index = current.random.val
        result.append((current.val, random_index))
        current = current.next
    print(result)

# Test cases
head1 = build_linked_list([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
copied_head1 = copyRandomList(head1)
print_linked_list(copied_head1)  # Output: [(7, None), (13, 7), (11, 1), (10, 11), (1, 7)]

head2 = build_linked_list([[1, 1], [2, 1]])
copied_head2 = copyRandomList(head2)
print_linked_list(copied_head2)  # Output: [(1, 2), (2, 2)]

head3 = build_linked_list([[3, None], [3, 0], [3, None]])
copied_head3 = copyRandomList(head3)
print_linked_list(copied_head3)  # Output: [(3, None), (3, 3), (3, None)]
