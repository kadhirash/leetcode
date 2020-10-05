# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        helper= ListNode(None)
        helper.next = head
        
        if not head:
            return head
        while head and head.next:
            if head.next.val > head.val:
                head = head.next # move pointer 
                continue # continue through the list 
                
            insert = head.next # the node needs to be inserted
            head.next = head.next.next # move head.next value to head.next.next
            
            # find the inserting position
            prev = helper
            while prev.next and prev.next.val<insert.val: # insert only if > prev.next.val 
                prev = prev.next # move prev pointer
            
            # inserting node via swap
            insert.next, prev.next = prev.next, insert

        return helper.next