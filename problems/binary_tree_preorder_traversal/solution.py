# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # recursive:
        # root, left, right
        # if not root:
        #     return []
        # else:
        #     return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        
        # iterative
        
        ans, stack = [],[]
        
        while stack or root:
            if root:
                ans.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return ans
    
    
    
    
                