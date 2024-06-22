# 226. Invert Binary Tree
# Given the root of a binary tree, invert the tree, and return its root.

 

# Example 1:


# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Example 2:


# Input: root = [2,1,3]
# Output: [2,3,1]
# Example 3:

# Input: root = []
# Output: []
#!NOTE: recurrively we will Go to left and right then we will swap it and we will continue till while root.left and root.right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: TreeNode) -> TreeNode:
    if root is None:
        return None
    
    # Swap the left and right children
    root.left, root.right = root.right, root.left
    
    # Recursively invert the left and right subtrees
    invertTree(root.left)
    invertTree(root.right)
    
    return root

# Helper function to print the tree in level order for easy verification
def print_tree(root):
    if not root:
        return []
    from collections import deque
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing Nones that don't affect the structure of the tree
    while result and result[-1] is None:
        result.pop()
    return result

# Example 1
root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(7)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(9)
print("Original tree:", print_tree(root1))
inverted_root1 = invertTree(root1)
print("Inverted tree:", print_tree(inverted_root1))

# Example 2
root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
print("Original tree:", print_tree(root2))
inverted_root2 = invertTree(root2)
print("Inverted tree:", print_tree(inverted_root2))

# Example 3
root3 = None
print("Original tree:", print_tree(root3))
inverted_root3 = invertTree(root3)
print("Inverted tree:", print_tree(inverted_root3))
