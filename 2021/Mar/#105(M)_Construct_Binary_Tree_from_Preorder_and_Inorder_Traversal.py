# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # if traversal has length one, then we have a one-noded tree
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        # root is the first elem of preorder traversal
        root = preorder[0]
        
        # find root's index in inorder traversal
        index = inorder.index(root)
        
        # find portions of the left tree
        in_left = inorder[:index]
        left_length = len(in_left)
        pre_left = preorder[1:left_length+1]
        
        left_tree = None if left_length == 0 else self.buildTree(pre_left, in_left)
        
        # find portions of the right tree
        in_right = inorder[index+1:]
        right_length = len(in_right)
        pre_right = preorder[1+left_length:]
        
        right_tree = None if right_length == 0 else self.buildTree(pre_right, in_right)
        
        return TreeNode(root, left_tree, right_tree)
