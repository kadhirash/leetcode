# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        if root is None:
            return True
        
        
        def checker(root: TreeNode, check_one: [], check_two: []) -> bool:
            if root is None:
                return True
            
            for i in check_one:
                if root.val >= i:
                    return False
            for i in check_two:
                if root.val <= i:
                    return False
                
            if not root.left and not root.right:
                return True
            
            return checker(root.left, check_one + [root.val], check_two) and checker(root.right, check_one, check_two + [root.val])

        if checker(root.left, [root.val], []) and checker(root.right, [], [root.val]):
            return True
        else:
            return False