# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # DFS to go down to different levels and see if exists on left, then on right and add it up
        
        max_width = 0 # variable to keep track of max width
        index_table = {} # hash map to keep track of indexes
        
        def DFS(node, depth, col_index): # classic DFS taking in node, depth, and column index
            nonlocal max_width
            if node is None: # if no Tree at all, return 0?
                return 0
            
            if depth not in index_table:    # if no depth in index table, set it to the col_index
                index_table[depth] = col_index
                
            max_width = max(max_width, col_index - index_table[depth] + 1)
            
            DFS(node.left, depth +1, 2* col_index)
            DFS(node.right, depth +1, 2*col_index+1)
            
        DFS(root,0,0)
        
        return max_width