# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l3 = ListNode(0)
        carry = 0
        
        while carry or l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            
            l3.val = carry % 10
            carry //= 10
            
            if carry or l1 or l2:
                l3.next = ListNode(0)
                l3 = l3.next
        return head
            