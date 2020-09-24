"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import collections
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root: return None
        
        queue = collections.deque()
        queue.append(root)
        ans = root
        
        while queue:
            size = len(queue)
            
            for i in range(size):
                
                root = queue.popleft()
                
                if i < size - 1:
                    root.next = queue[0]
                    
                if root.left:
                    queue.append(root.left)
                    
                if root.right:
                    queue.append(root.right)
                
        return ans

    
    
    
    
    