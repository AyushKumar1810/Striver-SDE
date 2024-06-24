# 108. Convert Sorted Array to Binary Search Tree
# Solved
# Easy
# Topics
# Companies
# Given an integer array nums where the elements are sorted in ascending order, convert it to a 
# height-balanced
#  binary search tree.

 

# Example 1:


# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:


# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    # Initialize the left and right pointers
        l = 0 
        r = len(nums) - 1

    # Calculate the middle index
        mid = (l + r) // 2

    # Base case: if the left pointer is greater than the right pointer, return None
        if l > r:
            return None

    # Create a new TreeNode with the value at the middle index
        root = TreeNode(nums[mid])

    # Recursively construct the left subtree
        root.left = self.sortedArrayToBST(nums[0:mid])

    # Recursively construct the right subtree
        root.right = self.sortedArrayToBST(nums[mid + 1 : r + 1])

    # Return the root node of the constructed binary search tree
        return root

#Basically we are using Bianary search 
