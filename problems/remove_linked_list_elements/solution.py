# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        def remove(node, val):
            if node:
                if node.val == val:
                    return remove(node.next,val)
                else:
                    node.next = remove(node.next,val)
            return node
        return remove(head,val)
    