# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # rotate to the right, k times
        
        if not head:
            return None

        curr = head
        nodes = 1
        while curr.next:
            curr = curr.next
            nodes += 1
        curr.next = head

        
        rotate_loc = nodes - (k % nodes)
        
        for i in range(rotate_loc):
            curr = curr.next

        prev = curr        
        curr = curr.next
        prev.next = None
       
        return curr