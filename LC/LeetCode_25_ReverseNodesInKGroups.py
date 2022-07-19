# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ---- Solution ------ #

class Solution(object):
    def reverseKGroup(self, head, k):
      dummy = ListNode(0, head) # Handle edges cases with dummy
      groupPrev = dummy # beginning of every group

      while True:
        kth = self.getKth(groupPrev, k) # grab last node in the group
        if not kth: # if kth out of bounds, done with algo
          break
        groupAfter = kth.next # grab the node to connect the beginning node to (draw it out)

        # Reverse linked list algo
        prev, curr = groupAfter, groupPrev.next # set first to the next group first
        while curr != groupAfter:
          after = curr.next
          curr.next = prev
          prev = curr
          curr = after
        # Tricky part
        tmp = groupPrev.next # grab the original first node which is now the group prev
                            # node in the next iteration
        groupPrev.next = kth # For dummy chain sake, set the dummy next to the kth node
        groupPrev = tmp # set the group prev now to the next iteration's group prev

      return dummy.next

    # helper function to get kth node
    def getKth(self, curr_node, k):
      while curr_node and k > 0:
        curr_node = curr_node.next
        k -= 1
      return curr_node