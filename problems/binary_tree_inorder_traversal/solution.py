# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        order, ans = [ ], [ ]
        
        while order or root:
            if root:
                order.append(root)
                root = root.left
            else:
                popped = order.pop()
                ans.append(popped.val)
                root = popped.right
        return ans