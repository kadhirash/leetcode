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
            m -= 1
            n -=1
            
        connect = prev
        tail = curr
        
        while n > 0:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            n -= 1
            
        if connect != None:
            connect.next = prev   
        else:
            head = prev
            
        tail.next = curr
        return head
            