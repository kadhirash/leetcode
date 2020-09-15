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
stack = [--4---5---6--NULL]


1---2---3- 7---8-11--12--NULL--9---10--NULL
'''
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        temp = head
        stack = []
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
        return temp
        