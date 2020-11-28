import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for curr in lists:
            while curr:
                heapq.heappush(heap,curr.val)
                curr = curr.next
                
        res = cur = ListNode(0)
        while heap:
            cur.next = ListNode(heapq.heappop(heap))
            cur = cur.next
        return res.next