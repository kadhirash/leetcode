"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import collections
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        copy = collections.defaultdict(lambda: Node(0))
        copy[None] = None
        node = head
        while node:
            copy[node].val = node.val
            copy[node].next = copy[node.next]
            copy[node].random = copy[node.random]
            node = node.next
        return copy[head]