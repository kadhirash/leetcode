# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # top to bottom, every other row -> left to right and right to left
        
        
        if not root: 
            return None
        
        queue = collections.deque()
        queue.append(root)
        
        ans = []
        
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