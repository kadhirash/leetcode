# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # def recursive(root):
        #     if not root: return None
        #     recursive(root.left)
        #     recursive(root.right)
        #     res.append(root.val)
        # res = []
        # recursive(root)
        # return res
        
        # iterative
        postorder, stack = [], []
        if not root: return None
        while root or stack:
            while root:
                stack.append(root)
                postorder.insert(0,root.val)
                root = root.right
            root = stack.pop()
            root = root.left
        return postorder