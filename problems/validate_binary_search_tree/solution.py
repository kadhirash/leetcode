# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    pre_node = TreeNode(float('-inf'))
    def isValidBST(self, root: TreeNode) -> bool:
        # q/a:
            # BT:
                # left < root < right
                # each level: 0 - 2 children
            # return None if no root
            
        # strat:
            # inorder traversal
            # pre_node = low value
            
            
#         stack = []
#         pre_node = float('-inf')
        
#         while stack or root:
            
#             if root:
#                 stack.append(root)
#                 root = root.left
#             else:
#                 root = stack.pop()
#                 if pre_node >= root.val:
#                     return False
#                 pre_node = root.val
#                 root = root.right
#         return True

        if not root:
            return True
            
        if not self.isValidBST(root.left):
            return False
        
        if self.pre_node and self.pre_node.val >= root.val:
            return False
        
        self.pre_node = root
        
        if not self.isValidBST(root.right):
            return False
        
        return True