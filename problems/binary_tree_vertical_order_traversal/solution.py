# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        # queue
        # hashmap -> store values
        # iterate thrgouh the min_col <-> max_col
            # return ans via the hashmap
        
        if not root:
            return []
        col_dict = collections.defaultdict(list)
        queue = collections.deque()
        queue.append((root,0)) # root, col #
        
        min_col = max_col = 0
        
        while queue:
            root,col = queue.popleft()
            
            if root.left:
                queue.append((root.left,col-1))
                min_col = min(min_col, col-1)
            
            if root.right:
                queue.append((root.right, col + 1))
                max_col = max(max_col, col + 1)
                
            col_dict[col].append(root.val)
        
        ans = []
        
        for i in range(min_col, max_col+1):
            ans.append(col_dict[i])
        return ans
        
            
        
        