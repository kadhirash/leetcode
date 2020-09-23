# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections 
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        ans = []
        queue = deque()
        
        if not root:
            return ans
        
        queue.append(root)
        while queue:
            size = len(queue)
            root_level = []
            
            for i in range(size):
                root = queue.popleft()
                root_level.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            ans.append(root_level)
        return ans