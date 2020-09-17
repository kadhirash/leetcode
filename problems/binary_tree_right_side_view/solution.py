# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # dfs level by level, but only collecting the right side nodes
        # bfs 
        
        
#         if not root: return None
        
#         right_side = []
#         stack = [(root,0)] # root, level
        
#         while stack:
#             node,level = stack.pop() # pop off the node and its corresponding level
#             if node:
#                 if len(right_side) <= level: # if right_side values are less than the current level, then add to it
#                     right_side.append(node.val)
#                 stack.append((node.left,level+1))
#                 stack.append((node.right,level+1))
#         return right_side
            
            if not root: return None
            
            right_side = []
            queue = deque([root,]) # queue 
            
            while queue:
                level_len = len(queue)
                
                for i in range(level_len):
                    node = queue.popleft() # pop off nodes from the front of queue -> O(1) time
                    if i == level_len - 1: # i == right_side level
                        right_side.append(node.val)
                        
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            return right_side