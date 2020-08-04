# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # inorder, stack = [], []
        # #node, stack = root, []
        # if not root: return inorder
        # while root or stack: 
        #     while root: 
        #         stack.append(root)
        #         root = root.left
        #         #continue
        #     root = stack.pop()
        #     inorder.append(root.val)
        #     root = root.right
        # return inorder
        res = []
        def recursive(root:TreeNode):
            if not root: return None
            recursive(root.left)
            res.append(root.val)
            recursive(root.right)
        recursive(root)
        return res
