"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
  def flatten(self, head):
    stack = []
    # Walk through the linked list until hitting the deepest tail node
    # Add toConnectNodes to stack
    curr = head
    while curr: # need only curr as it could be childs all the way down (next pointer is None each level)
      if curr.child:
        if curr.next:
          stack.append(curr.next)
          curr.next.prev = None # break connection with toConnectNode
        # Set double LL pointers with curr and child
        curr.next = curr.child
        curr.child.prev = curr
        curr.child = None

      # we need a non-None curr node; break the while loop once we hit the end of the walk through the
      # child path
      if curr.next:
        curr = curr.next
      else:
        break

    while stack:
      nextNode = stack.pop()
      curr.next = nextNode # connect nodes pointers
      nextNode.prev = curr # connect nodes pointers
      while curr.next:
        curr = curr.next

    return head