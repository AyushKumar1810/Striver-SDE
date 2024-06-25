# 98. Validate Binary Search Tree

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left 
# subtree
#  of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [2,1,3]
# Output: true
# Example 2:


# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#NOTE:#* easy we will use recurrsion we will compare rootnode with left node and right node and we will see if root.val > root.left.val and root.val < root.right.val then it's a Binary search tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: TreeNode) -> bool:
    def validate(node, low=-float('inf'), high=float('inf')):
        # An empty tree is a valid BST
        if not node:
            return True
        # The current node's value must be within the range [low, high]
        if not (low < node.val < high):
            return False
        # Recursively validate the left and right subtrees
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)
    
    return validate(root)

        
# def isValidBST(root: TreeNode) -> bool:
#     def validate(node, left=-float('inf'), right=float('inf')):
#         if not node:
#             return True
#         if not (node.left < node.val<node.right):
#             return  False
#         return (validate(node.left , left , node.val) and validate(node.right , node.val,right))
#     return validate(root)