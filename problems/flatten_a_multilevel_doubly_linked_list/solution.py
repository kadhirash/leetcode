"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
'''
stack = [---4---5---6--NULL,]

1---2---3<->7---8<-> 11--12----9---10--NULL ..

'''
class Solution:
    
    def flatten(self, head: 'Node') -> 'Node':
        def fn(node, default=None):
            """Return head of (recursively) flattened linked list"""
            if not node: 
                return default 
            node.next = fn(node.child, fn(node.next, default))
            if node.next: 
                node.next.prev = node
            node.child = None
            return node
        
        return fn(head)
        