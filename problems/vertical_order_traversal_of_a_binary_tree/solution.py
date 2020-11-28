# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        col_dict = collections.defaultdict(list)
        
        queue = collections.deque()
        queue.append((root,0))
        
        min_col = max_col = 0
        
        while queue:
            size = len(queue)
            temp_dict = collections.defaultdict(list)
            
            for i in range(size):
                root,col = queue.popleft()
                
                if root.left:
                    queue.append((root.left,col-1))
                    min_col = min(min_col, col-1)
                    
                if root.right:
                    queue.append((root.right, col+ 1))
                    max_col = max(max_col, col + 1)
                    
                temp_dict[col].append(root.val)
            
            for i in temp_dict:
                col_dict[i] += sorted(temp_dict[i])
        
        ans = []
        
        for i in range(min_col, max_col + 1):
            ans.append(col_dict[i])
        return ans