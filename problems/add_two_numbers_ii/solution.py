# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # create two stacks
        stack_one, stack_two = [], []
        
        # add ListNode values to both stacks
        while l1:
            stack_one.append(l1.val)
            l1 = l1.next
        while l2:
            stack_two.append(l2.val)
            l2 = l2.next
        
        # sum_carry variable to hold the sum AND carry
        sum_carry = 0
        ans = ListNode(0) # create a ListNode pointer to hold the ans
        
        # while values exist in either stack
        while len(stack_one) > 0 or len(stack_two) > 0:
            # if value exists in first stack, pop off value and add to sum_carry
            if len(stack_one) > 0:
                sum_carry += stack_one.pop()
                
            if len(stack_two) > 0:
                sum_carry += stack_two.pop()
                
            
            # get the value of carry and hold it in the ans.val
            ans.val = sum_carry % 10 
            # create head node to store carry
            head = ListNode(sum_carry // 10)
            # swap head node and ans
            head.next = ans
            ans = head
            
            sum_carry //= 10 # store carry in sum_carry
            
        if ans.val == 0: # if ans = 0, return ans.next 
            return ans.next
        else:
            return ans
            
            