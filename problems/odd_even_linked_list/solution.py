# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        odd,even = head, head.next
        even_head = head.next
        while even and even.next:
            odd.next = even.next # 1 ""-->"" 3
            odd = odd.next # 1 -> 2
            even.next = odd.next # 2 ""-->"" 4
            even = even.next # 2-> 3
        odd.next = even_head
        return head
        
            