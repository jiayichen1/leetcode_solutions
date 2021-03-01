# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.lca, self.found = None, False
        
        self.findHelper(root, p.val, q.val)
        
        return self.lca
    
    def findHelper(self, root, p, q):
        num_found = 0
        
        if root.left:
            num_found += self.findHelper(root.left, p, q)
        
        if root.right:
            num_found += self.findHelper(root.right, p, q)
        
        if root.val == p or root.val == q:
            num_found += 1
        
        if num_found == 2 and not self.found:
            self.lca = root
            self.found = True
        
        return num_found

    # less straightforward recursive solution
    # most code from leetcode.cn discussion board
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # base case
        if root == None:
            return None
        
        # short circuiting
        # NOT SURE why it's done like this
        if root.val == p.val or root.val == q.val:
            return root
        
        lNode = self.lowestCommonAncestor2(root.left, p, q)
        rNode = self.lowestCommonAncestor2(root.right, p, q)
        
        if lNode and rNode:
            return root
        elif lNode:
            return lNode
        else:
            return rNode
        
        return None
        