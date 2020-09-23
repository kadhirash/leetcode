# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 2 stacks 
        # val % 10 
        # carry 
        
        
        s1, s2 = [], []
        
        while l1 or l2:
            if l1:
                s1.append(l1.val)
                l1 = l1.next
            if l2:
                s2.append(l2.val)
                l2 = l2.next
                
        
        head = ListNode(0)
        carry = 0
        
        while s1 or s2:
            if s1:
                carry += s1.pop()
            if s2:
                carry += s2.pop()
                
            head.val = carry % 10
            temp = ListNode(carry // 10)
            temp.next = head
            head = temp
            carry //= 10
            
        
        if head.val == 0:
            return head.next
        else:
            return head