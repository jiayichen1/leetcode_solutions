# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        
        res, nodeStack = [], []
        nodeStack.append(root.right)
        nodeStack.append(root.val)
        nodeStack.append(root.left)
        
        while len(nodeStack) > 0:
            node = nodeStack.pop()
            if node == None:
                if len(nodeStack) != 0:
                    res.append(nodeStack.pop())
                continue
                
            nodeStack.append(node.right)
            nodeStack.append(node.val)
            nodeStack.append(node.left)
        
        return res
                