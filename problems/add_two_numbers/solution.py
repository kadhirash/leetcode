# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = temp = ListNode(0)
        carry = 0
        
        while l1 or l2 or carry:
            if l1:
                val1 = l1.val 
            else:
                val1 = 0
            
            if l2:
                val2 = l2.val
            else:
                val2 = 0
            
            curr_sum = val1 + val2 + carry
            
            node = ListNode(curr_sum % 10)
            carry = curr_sum // 10
            
            temp.next = node # poiints to curr node
            temp = temp.next # update temp traversal
            
            if l1:
                l1 = l1.next
            else:
                l1 = None
                
            if l2:
                l2 = l2.next
            else:
                l2 = None
                
        return l3.next
            