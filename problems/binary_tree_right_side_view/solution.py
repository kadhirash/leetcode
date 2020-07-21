# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # use a stack to store nodes
        # SOLUTION FAILS, ONLY GETS RIGHT NODES, but you want all nodes you see from right side
#         if not root:
#             return [ ]
#         ans = [ ]
#         ans.append(root.val)
        
#         while root.right:
#             ans.append(root.right.val)
#             root = root.right
#         return ans
#left_sub_nodes[len(right):]

# strategy 2: collect all nodes level traversal, use stack
        
        if not root: # if root is None
            return [ ] # return empty stack
        ans = [ ]
        ans.append(root.val) # append root val to this
        #print(ans)
        # right view of left sub tree
        left_sub_nodes = ans + self.rightSideView(root.left)
        print(f' right view, left sub tree nodes: {left_sub_nodes}')
        #right view of right sub tree
        right_sub_nodes = ans + self.rightSideView(root.right)
        print(f' right view, right sub tree nodes: {right_sub_nodes}')
        # after getting both sides of the nodes, combine them
        #print(len(right_sub_nodes))
        #return right_sub_nodes + left_sub_nodes # prints extra nodes
        
        # have extra variable for blocked view on the left sub_tree to only get non blocked nodes 
        skip_block = left_sub_nodes[len(right_sub_nodes):]
        # print(f'skip block: {skip_block}')
        return right_sub_nodes + skip_block
        