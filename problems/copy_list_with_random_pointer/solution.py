"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        '''Clone a doubly linked list with random pointer'''
        '''with O(1) extra space'''

        '''Insert additional node after every node of original list'''
        if not head: return None
        curr = head 
        while curr != None: 
            new = Node(curr.val) 
            new.next = curr.next
            curr.next = new 
            curr = curr.next.next

        '''Adjust the random pointers of the newly added nodes'''
        curr = head 
        while curr != None:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        '''Detach original and duplicate list from each other'''
        curr = head 
        dup_root = head.next
        while curr.next != None: 
            tmp = curr.next
            curr.next = curr.next.next
            curr = tmp 

        return dup_root 
    
        