# 617. Merge Two Binary Trees
# You are given two binary trees root1 and root2.

# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

# Return the merged tree.

# Note: The merging process must start from the root nodes of both trees.

 

# Example 1:


# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]
# Example 2:

# Input: root1 = [1], root2 = [1,2]
# Output: [2,2]
#NOTE: #* The thing is that we have to to use recurrsuion of left and right od both tree given and for better space complexivity we can update in of the given two tree root1.left= root1.left + root2.left
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(root1: TreeNode, root2: TreeNode) -> TreeNode:
    if not root1 and not root2:
        return None
    if not root1:
        return root2
    if not root2:
        return root1
    
    # Merge the values of the two nodes
    merged = TreeNode(root1.val + root2.val)
    
    # Recursively merge the left and right children
    merged.left = mergeTrees(root1.left, root2.left)
    merged.right = mergeTrees(root1.right, root2.right)
    
    return merged

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
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)

merged_root = mergeTrees(root1, root2)
print("Merged tree:", print_tree(merged_root))

# Example 2
root1 = TreeNode(1)

root2 = TreeNode(1)
root2.left = TreeNode(2)

merged_root = mergeTrees(root1, root2)
print("Merged tree:", print_tree(merged_root))
