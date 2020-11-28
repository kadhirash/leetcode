# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        s = []
        while root != None or len(s) > 0:
            while root != None:
                s.append(root)
                root = root.left
            
            root = s[-1]
            s.pop()
            
            
            k -=1
            if k == 0:
                return root.val 
        
            root = root.right
            
        return -1