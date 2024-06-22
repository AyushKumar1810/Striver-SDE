# 1448. Count Good Nodes in Binary Tree

# Hint
# *Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.

 

# Example 1:



# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.
# Example 2:



# Input: root = [3,3,null,4,2]
# Output: 3
# Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
# Example 3:

# Input: root = [1]
# Output: 1
# Explanation: Root is considered as good.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node, max_val):
            if not node:

                return 0
            # Check if the current node is a good node
            good = 1 if node.val >= max_val else 0
            # Update the maximum value on the path to the current node
            max_val = max(max_val, node.val)
            # Recursively count good nodes in the left and right subtrees
            good += dfs(node.left, max_val)
            good += dfs(node.right, max_val)
            return good
        
        # Start DFS traversal from the root
        return dfs(root, root.val) if root else 0

# Test cases

# Example 1: Input: [3,1,4,3,null,1,5]
root1 = TreeNode(3)
root1.left = TreeNode(1, TreeNode(3))
root1.right = TreeNode(4, TreeNode(1), TreeNode(5))
print(Solution().goodNodes(root1))  # Output: 4

# Example 2: Input: [3,3,null,4,2]
root2 = TreeNode(3)
root2.left = TreeNode(3, TreeNode(4), TreeNode(2))
print(Solution().goodNodes(root2))  # Output: 3

# Example 3: Input: [1]
root3 = TreeNode(1)
print(Solution().goodNodes(root3))  # Output: 1
