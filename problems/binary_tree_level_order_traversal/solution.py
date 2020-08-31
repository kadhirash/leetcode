# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root: return ans
        def bfs(node, level):
            if node:
                if len(ans) == level:
                    ans.append([])
                ans[level]+=[node.val]
                bfs(node.left, level + 1)
                bfs(node.right, level + 1)
        bfs(root,0)
        return ans