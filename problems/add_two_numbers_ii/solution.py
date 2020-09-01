# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack_1, stack_2 = [],[]
        temp1 = l1
        while l1:
            stack_1.append(l1.val)
            l1 = l1.next
        temp1 = l2
        while l2:
            stack_2.append(l2.val)
            l2 = l2.next
        
        carry, ans, head = 0, [], ListNode(-1)
        while stack_1 or stack_2:
            if not stack_1:
                val = stack_2.pop()
            elif not stack_2:
                val = stack_1.pop()
            else:
                val = stack_1.pop() + stack_2.pop()
            carry,val = divmod(carry+val, 10)
            head.val = val
            temp = head
            head = ListNode(-1)
            head.next = temp
        if carry:
            head.val = carry
        return head if head.val != -1 else head.next
            