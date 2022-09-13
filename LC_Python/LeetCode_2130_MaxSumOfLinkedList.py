# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution(object):
  def pairSum(self, head):
    slow, fast = head, head
    while fast and fast.next:
      slow, fast = slow.next, fast.next.next
    secondHead = self.revLL(slow)

    res = float('-inf')
    while head and secondHead:
      first, second = head.val, secondHead.val
      res = max(res, first+second)
      head, secondHead = head.next, secondHead.next
    return res


  def revLL(self, node):
    prev = None
    while node:
      after = node.next
      node.next = prev
      prev = node
      node = after
    return prev
