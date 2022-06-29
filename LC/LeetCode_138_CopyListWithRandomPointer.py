
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        oldToNew = { None : None } # copying graphs or LLs requires a old-to-new dict

        # Map just the nodes, so new node with old node's value
        cur = head
        while cur: # while there are still nodes to look at
          oldToNew[cur] = Node(cur.val) # old node is mapped to new hallow node with only value
          cur = cur.next

        # Set pointers
        # need to break it up into 2 for loops so we can set the forward pointers
        # to THE COPIED NODES which we constructed in the first loop
        cur = head
        while cur:
          oldToNew[cur].next = oldToNew[cur.next]
          oldToNew[cur].random = oldToNew[cur.random]
          cur = cur.next

        return oldToNew[head]