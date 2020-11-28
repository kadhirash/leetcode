"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        dummy_node = Node(0,None,None)
        print(f'dummy_node: {dummy_node.val}')
        prev = dummy_node
        print(f'prev: {prev.val}')
        current = root
        print(f'current: {current.val}')
        result = [ ]
        while True:
            if current is not None:
                result.append(current)
                current = current.left
                print(f'while current: {current}')
            elif(result):
                current = result.pop()
                current.left,prev.right, prev = prev, current,current
                current = current.right
                print(f'result current: {current}')
            else:
                dummy_node.right.left, prev.right = prev, dummy_node.right
                print(f'dummy_node.right.left:{dummy_node.right.left.val}, prev.right: {prev.right.val}')
                break
        print(f'dummy_node.right: {dummy_node.right.val}')
        return dummy_node.right