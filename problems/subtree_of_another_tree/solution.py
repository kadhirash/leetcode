# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        tree1, tree2 = self.preorder(s), self.preorder(t)
        return tree2 in tree1
    def preorder(self, t: TreeNode) -> bool:
        if not t: return "None"
        return "#" + str(t.val) + " " + self.preorder(t.left) + " " + self.preorder(t.right)