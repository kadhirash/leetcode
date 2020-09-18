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
1---2---3 <-> 7---8<--->11--12<--->--9<---10-->-4---5---6--NULL,


'''
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return head
        
        pseudo_head = Node(None,None, head,None)
        self.flatten_dfs(pseudo_head, head)
        
        pseudo_head.next.prev = None
        return pseudo_head.next
    
    def flatten_dfs(self, prev,curr):
        if not curr: return prev # tail of flatten list
        
        curr.prev = prev
        prev.next = curr 
        
        temp_next = curr.next
        tail = self.flatten_dfs(curr, curr.child)
        curr.child = None
        return self.flatten_dfs(tail, temp_next)
        
        