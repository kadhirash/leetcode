# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 1 -> 2 -> 3 -> 4 -> 5 -> NULL
        # NULL <- 1 <- 2 <- 3 <- 4 <- 5
        
        # head = linked list 
        # dummy node = None
        
        # curr_node = ListNode(head.val) # creates a current_node at the first val of head
        # head.next = dummy_node
        # dummy_node<- 1(head/curr_node)   2 -> 3 -> 4 -> 5 -> NULL
        # curr_node = head.next
        # dummy_node = curr_node
        
        
#         dummy_node = None
            
            
#         while head != None:
#             curr_node = ListNode(head.val)
#             curr_node.next = dummy_node
#             head = head.next
#             dummy_node = curr_node
#         return dummy_node
        
    
        if not head or not head.next:
            return head
        else:
            dummy = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return dummy

        