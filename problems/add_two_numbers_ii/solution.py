# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # q/a:
            # return 0 if no l1 or l2
            
        # strat:
            # 2 stacks
                # l1, l2
            # LIFO -> pop
            # % 10 
            # //10 
        
        # if not l1 or not l2:
        #     return None
        
        s1,s2 = [], []
        
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
                
            ans.val = carry % 10
            temp = ListNode(carry // 10) # [0,7]
            temp.next = ans # [7]
            ans = temp # [0,7]
            carry //= 10
            
        if ans.val == 0: #[0,7,8,0,7]
            return ans.next
        else:   # [7,8,0,7]
            return ans
            