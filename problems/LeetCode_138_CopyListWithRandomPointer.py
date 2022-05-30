"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = { None : None }

        # Map just the nodes to be then referenced when setting pointers
        cur = head
        while cur:
          oldToNew[cur] = Node(cur.val)
          cur = cur.next

        # Set pointers
        cur = head
        while cur:
          oldToNew[cur].next = oldToNew[cur.next]
          oldToNew[cur].random = oldToNew[cur.random]
          cur = cur.next

        return oldToNew[head]