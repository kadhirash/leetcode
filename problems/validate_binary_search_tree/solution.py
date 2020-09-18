# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # inorder traversal
            # left > root > right
        
        # ex: [2,1,3]
            # true
        
        return self.validate(root,None,None)
    
    
    def validate(self, root: TreeNode, maxi: int, mini: int) -> bool:
        
        if not root: return True
        
        elif (maxi != None and root.val >= maxi) or (mini != None and root.val <= mini):
            return False
        else:
            return self.validate(root.left,root.val,mini) and self.validate(root.right, maxi,root.val)
        
        
                
        