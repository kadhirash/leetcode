# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        ans = []
        
        self.in_order(root, ans)
        
        for i in range(1,len(ans)):
            if ans[i-1] >= ans[i]:
                return False
        return True
    
    def in_order(self, node: TreeNode, output: List[int]) -> None:
        if not node:
            return 
        
        self.in_order(node.left, output)
        output.append(node.val)
        self.in_order(node.right, output)