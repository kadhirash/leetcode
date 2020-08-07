# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s: return False
        if self.sameTree(s,t):
            return True
        else:
            left = self.isSubtree(s.left, t)
            right = self.isSubtree(s.right, t)
            return left or right
    def sameTree(self, node1: TreeNode, node2: TreeNode) -> bool:
        if node1 != None and node2 != None:
            if node1.val == node2.val:
                left = self.sameTree(node1.left, node2.left)
                right = self.sameTree(node1.right, node2.right)
                return left and right
            else:
                return False
        else:
            if not node1 and not node2:
                return True
            return False
        
        
        
    
    