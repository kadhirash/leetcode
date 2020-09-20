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
        # strat:
            # stack to hold head.next nodes
            
        self.recursively_flatten(head)
        return head
    
    # Takes the head of the list to be flattened, and returns the tail of the flattened list.
    def recursively_flatten(self, head):
        
        # Could happen if outer caller passes in an empty list.
        if head == None:
            return None
        
        # Base case - there is nothing left to flatten.
        if head.next == None and head.child == None:
            return head
        
        # Recursive case - we need to flatten the child and the tail.
        tail = head.next # We need to store this as doing child first.
        current_end = head # Where will we be attaching next?
        
        if head.child != None:
            child_end = self.recursively_flatten(head.child)
            self.link(current_end, head.child)
            current_end = child_end
            head.child = None
            
        if tail != None:
            tail_end = self.recursively_flatten(tail)
            self.link(current_end, tail)
            current_end = tail_end
            
        return current_end
    
    def link(self, node_1, node_2):
        node_1.next = node_2
        node_2.prev = node_1
        