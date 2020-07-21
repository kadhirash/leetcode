# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # iterate through the linkedList
        # if val exists, then delete
            # 1 --> "val" --> 3->4 
            # 1 --> 3 -->4  
                # 1.next = val.next
                # val.next = None
      
        dummy = ListNode(0)
        dummy.next = head
        
        prev, curr = dummy, head
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = prev.next
            else:
                prev = curr
                curr = curr.next
            
        return dummy.next
        