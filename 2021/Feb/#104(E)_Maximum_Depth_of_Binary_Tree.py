# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Bottom up recursion
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        elif not root.left and not root.right:
            return 1
        
        ld, rd = self.maxDepth(root.left), self.maxDepth(root.right)
        return max(ld, rd) + 1
    