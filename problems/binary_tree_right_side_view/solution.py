# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        
        queue = collections.deque()
        
        queue.append(root)
        
        ans = []
        while queue:
            size = len(queue)
            
            for i in range(size):
                root = queue.popleft()
                
                if i == size -1:
                    ans.append(root.val)
                
                if root.left:
                    queue.append(root.left)
                    
                if root.right:
                    queue.append(root.right)
        return ans