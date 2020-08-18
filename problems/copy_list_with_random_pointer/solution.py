"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # TC: O(n), SC: O(1) extra space
        if not head:
            return None

        node = head

        while node:
            next = node.next
            copy = Node(node.val, node.next, node.random)
            node.next = copy
            copy.next = next
            node = next

        node = head

        while node:
            if node.random:
                node.next.random = node.random.next

            node = node.next.next

        dummy = Node(0)
        prev = dummy
        node = head

        while node:
            prev.next = node.next
            node.next = node.next.next
            node = node.next
            prev = prev.next

        return dummy.next