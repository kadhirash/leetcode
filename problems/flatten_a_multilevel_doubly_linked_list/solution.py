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
 stack = [ ] 
 temp   3r
 1---2---3 <-> 7---8<->11--12-->---9---10-->---4---5---6--NULL,
             
             
             


'''
class Solution:
    
    def flatten(self, head: 'Node') -> 'Node':
        stack = []
        ans = head
        
        while head:
            if head.child:
                if head.next:
                    stack.append(head.next)
                head.next = head.child
                head.next.prev = head
                head.child = None
            elif not head.next and stack:
                head.next = stack.pop()
                head.next.prev = head
            head = head.next 
        return ans
        
        