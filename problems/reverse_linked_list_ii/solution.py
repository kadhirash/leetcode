# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head == None:
            return None
        prev, curr = None, head
        
        while m > 1:
            prev = curr
            curr = curr.next
            m, n = m-1, n-1
            
        con, tail = prev, curr
        
        while n > 0:
            third = curr.next
            curr.next = prev
            prev = curr
            curr = third
            n -= 1
        
        if con:
            con.next = prev
        else:
            head = prev
        
        tail.next = curr
        
        return head