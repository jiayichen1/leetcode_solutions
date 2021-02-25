# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	# Iterative method
	# from https://www.youtube.com/watch?v=qT65HltK2uE
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        if root == None:
            return res
        
        stack1, stack2 = [], []
        stack1.append(root)
        
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        
        while stack2:
            res.append(stack2.pop().val)
        
        return res

# recursive method:
#        
#         res = []
        
#         if root == None:
#             return res
        
#         res += self.postorderTraversal(root.left)
#         res += self.postorderTraversal(root.right)
#         res.append(root.val)
        
#         return res
        