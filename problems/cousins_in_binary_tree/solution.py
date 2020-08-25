# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q = collections.deque()
        nodeMap = collections.defaultdict()
        q.append((root,0,0))
        
        while q:
            if x in nodeMap and y in nodeMap:
                break
            node, level, parent = q.popleft()
            nodeMap[node.val] = [level,parent]
            
            if node.left:
                q.append((node.left, level + 1, node.val))
            
            if node.right:
                q.append((node.right, level + 1, node.val))
                
        if nodeMap[x][0] == nodeMap[y][0] and nodeMap[x][1] != nodeMap[y][1]:
            return True
        return False