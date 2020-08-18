# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s: return False
        elif self.isSametree(s,t): return True
        else: return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
            
            
    def isSametree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s or not t: return s == None and t == None
        elif s.val == t.val: return self.isSametree(s.left, t.left) and self.isSametree(s.right, t.right)
        else: return False