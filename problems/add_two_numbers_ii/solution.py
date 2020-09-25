# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # ex:
            # 1->2->3 + 4->5->6 = 5->7->9
       # strat:
            # 2 stacks
            # ans_node + sum/carry
            
             
        s1, s2 = [], []
        
        while l1 or l2:
            if l1:
                s1.append(l1.val)
                l1 = l1.next
            if l2:
                s2.append(l2.val)
                l2 = l2.next
                
        ans = ListNode(0)
        carry = 0 
        
        
        while s1 or s2:
            if s1:
                carry += s1.pop()
            if s2:
                carry += s2.pop()
                
            
            ans.val = carry % 10 # 9
            temp = ListNode(carry // 10) # 0 or 1  --> 0    -> [0,9] after temp.next = ans
            temp.next = ans # 9
            ans = temp # [0,9]
            carry //= 10
            
        if ans.val == 0:
            return ans.next
        else:
            return ans