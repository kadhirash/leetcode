# Definition for a binary tree node.
# class TreeNode:
#      def __init__(self, val,left,right):
#          self.val = val
#          self.left = left
#          self.right = right


class Solution:
    def dfs(self, root, result):
        if root:
            result.append(root.val)
            self.dfs(root.left, result)
            self.dfs(root.right, result)
            
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = [ ]
        self.dfs(root,result)
        return result
    
    