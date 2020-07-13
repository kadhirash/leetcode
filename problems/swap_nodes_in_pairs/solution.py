# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 1 --> 2 --> 3 --> 4 --> None
        
        # 1 => head_swap ===> 3
        # 3 => head_next_swap ==> None
        
        # swap the values w/ recursion 
        
        if head == None or head.next == None:
            return head
        
        head_swap = head 
        head_next_swap = head.next
        
        head_swap.next = self.swapPairs(head_next_swap.next)
        head_next_swap.next = head_swap # actual swapping
        
        return head_next_swap