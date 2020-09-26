# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        
        col_dict = defaultdict(list)
        queue = deque()
        queue.append((root,0)) # append root and it's col
        
        min_col = max_col = 0
        
        while queue:
            node,col = queue.popleft()
            
            if node.left:
                queue.append((node.left, col-1))
                min_col = min(min_col, col-1)
                
            if node.right:
                queue.append((node.right, col+1))
                max_col = max((max_col, col+1))
                
            col_dict[col].append(node.val) # add the node's values at it's col key
    
        columns = []
        
        for i in range(min_col, max_col + 1):
            columns.append(col_dict[i])
        return columns
        
        
        
        
        
        
        
        
    