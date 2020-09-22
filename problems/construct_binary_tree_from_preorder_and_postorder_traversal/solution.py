# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    pre_index, post_index = 0,0
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        root = TreeNode(pre[self.pre_index])
        self.pre_index += 1
        
        if root.val != post[self.post_index]:
            root.left = self.constructFromPrePost(pre,post)
        if root.val != post[self.post_index]:
            root.right = self.constructFromPrePost(pre,post)
            
        self.post_index += 1
        return root
    

    
    
    
    
    
    # if not pre or not post: return None
    #     root = TreeNode(pre[0])
    #     if len(post) == 1: return root
    #     idx = pre.index(post[-2])
    #     root.left = self.constructFromPrePost(pre[1: idx], post[:(idx - 1)])
    #     root.right = self.constructFromPrePost(pre[idx: ], post[(idx - 1):-1])
    #     return root