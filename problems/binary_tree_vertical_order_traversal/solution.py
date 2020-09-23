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
        
        column_dict = defaultdict(list)
        queue = deque([(root, 0)])
        min_col = max_col = 0
        
        while queue:
            
            node, col = queue.popleft()
            
            if node.left:
                queue.append((node.left, col - 1))
                min_col = min(min_col, col - 1)
                
            if node.right:
                queue.append((node.right, col + 1))
                max_col = max(max_col, col + 1)
                
            column_dict[col].append(node.val)
            
            
        columns = []
        for i in range(min_col,max_col+1):
            columns.append(column_dict[i])
        return columns