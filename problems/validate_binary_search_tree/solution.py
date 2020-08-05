# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        if root is None:
            return True
        
        s = []
        prev = None
        
        while root != None or len(s) != 0:
            while root != None:
                s.append(root)
                root = root.left
            
            root = s[-1] 
            s.pop()
            if prev != None and prev.val >= root.val:
                return False
            prev = root
            root = root.right
            
            
        return True