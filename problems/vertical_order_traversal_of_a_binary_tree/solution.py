# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root: return None
        
        col_dict = defaultdict(list)
        queue = deque([(root,0)])
    
        min_col = max_col = 0
        
        while queue:
            size = len(queue)
            temp_dict = defaultdict(list)
            for _ in range(size):
                node, col= queue.popleft()
                temp_dict[col].append(node.val)
            
                if node.left:
                    queue.append((node.left, col - 1))
                    min_col = min(min_col, col - 1)
                
                if node.right:
                    queue.append((node.right, col + 1))
                    max_col = max(max_col, col + 1)
                
            for i in temp_dict:
                col_dict[i] += sorted(temp_dict[i])
        ans = []
        for i in range(min_col, max_col+1):
            ans.append(col_dict[i])
        return ans