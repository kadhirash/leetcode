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

        if not root: return
        
    
        
        while root:
            
            if root.left:
                
                # find rightmost
                right_most = root.left
                while right_most.right:
                    right_most = right_most.right
                    
                    
                # rewire connections
                right_most.right = root.right
                root.right = root.left
                root.left = None
                
                
            # right side of tree
            root = root.right