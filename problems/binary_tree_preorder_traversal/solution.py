# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return [ ]
        order, ans = [ ], [root]
        
        while ans:
            popped = ans.pop()
            #print(popped)
            order.append(popped.val)
            if popped.right:
                ans.append(popped.right)
            if popped.left:
                ans.append(popped.left)
        return order