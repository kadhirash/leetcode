# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #recursive
#         if not l1: return l2
#         if not l2: return l1
#         if not l1 and not l2: return None
        
#         while l1 and l2:
#             if l1.val <= l2.val:
#                 l1.next = self.mergeTwoLists(l1.next, l2)
#                 return l1
#             else:
#                 l2.next = self.mergeTwoLists(l1, l2.next)
#                 return l2
        #iterative
        l3 = ListNode(-1)
        head = l3
        
        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        head.next = l1 or l2
        return l3.next