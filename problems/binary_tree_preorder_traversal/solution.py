# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # # recursive
        # def recursive(root: TreeNode) -> List[int]:
        #     if not root: return None
        #     res.append(root.val)
        #     recursive(root.left)
        #     recursive(root.right)
        # res = []
        # recursive(root)
        # return res
        
        #iterative
        preorder, stack = [], []
        if not root: return None
        while root or stack:
            while root:
                stack.append(root)
                preorder.append(root.val)
                root = root.left
            root = stack.pop()
            root = root.right
        return preorder       