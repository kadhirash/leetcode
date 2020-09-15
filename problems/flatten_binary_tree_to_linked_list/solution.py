# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        
        
        
        def helper(root):
            if root is None:
                return None
            
            if root.left is None and root.right is None:
                return root
            
            lt = helper(root.left)
            rt = helper(root.right)
            
            if lt:
                lt.right = root.right
                root.right = root.left
                root.left = None
            
            return rt if rt else lt
        return helper(root)