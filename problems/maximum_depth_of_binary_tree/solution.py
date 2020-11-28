# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # dfs pre-order
        if root is None:
            return 0
        else:
            left_level = self.maxDepth(root.left)
            right_level = self.maxDepth(root.right)
            
            if(right_level > left_level):
                return right_level + 1
            else:
                return left_level + 1
           # return max(right_level + 1, left_level + 1)
       
           