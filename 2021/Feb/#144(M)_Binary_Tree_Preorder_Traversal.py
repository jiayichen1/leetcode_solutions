# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
        
#         if root == None:
#             return res
        
#         res.append(root.val)
#         res += self.preorderTraversal(root.left)
#         res += self.preorderTraversal(root.right)
        
#         return res

        if root == None:
            return []
        
        res, nodeStack = [], []
        nodeStack.append(root)
        
        while len(nodeStack) > 0:
            node = nodeStack.pop()
            if node == None:
                continue
            res.append(node.val)
            
            nodeStack.append(node.right)
            nodeStack.append(node.left)
        
        return res
        
        