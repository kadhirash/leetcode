# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        ans = [head]
        while ans[-1].next != None: 
            ans.append(ans[-1].next)
        return ans[len(ans)//2]