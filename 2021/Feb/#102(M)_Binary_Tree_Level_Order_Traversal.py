# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q = deque()
        res = []
        level = [root]
        
        while root and level:
            thisLevel, nextLevel = [], []
            
            for node in level:
                thisLevel.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            
            res.append(thisLevel)
            level = nextLevel
        
        return res
        