# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return None
        ans = [] 
        
        queue = collections.deque()
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
        
        for i in range(1,len(ans),2):
            ans[i].reverse()
        return ans