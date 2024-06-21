# 110. Balanced Binary Tree

# Given a binary tree, determine if it is 
# height-balanced
# .

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]

# Example 1: Balanced tree
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
# Input: [3,9,20,null,null,15,7]
# Output: True
print(Solution().isBalanced(root1))  # Output: True

# Example 2: Unbalanced tree
root2 = TreeNode(1)
root2.left = TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3))
root2.right = TreeNode(2)
# Input: [1,2,2,3,3,null,null,4,4]
# Output: False
print(Solution().isBalanced(root2))  # Output: False

# Example 3: Empty tree
root3 = None
# Input: []
# Output: True
print(Solution().isBalanced(root3))  # Output: True
