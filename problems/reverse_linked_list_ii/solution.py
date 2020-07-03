# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m == n: 
            return head
        p = dummy = ListNode()
        
        dummy.next = head
        
        for _ in range(m-1):
            p = p.next
        
        tail = p.next
            
        for _ in range(n-m):
            temp = p.next
            p.next = tail.next
            tail.next = tail.next.next
            p.next.next = temp
            
        return dummy.next