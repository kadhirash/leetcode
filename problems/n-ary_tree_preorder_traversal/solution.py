"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
#         if not root:
#             return [ ]
#         else:
#             ans = [ ]
#             ans.append(root.val)
            
#             for child in root.children:
#                 ans += self.preorder(child)
                
#         return ans
          
            if not root: return None
            ans = [ ]
            stack = [root]
            while stack:
                curr = stack.pop()
                ans.append(curr.val)
                stack.extend(reversed(curr.children))
            return ans