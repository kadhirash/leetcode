# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
         # 2 pointers
                # pointA, pointB
                
                
            if not headA or not headB:
                return None
            
            pA, pB = headA, headB
            
            while pA != pB:
                pA = pA.next
                pB = pB.next
                
                if pA == pB:
                    return pA
                
                if not pA:
                    pA = headB
                if not pB:
                    pB = headA
                
                
            return pA
            
            
                    