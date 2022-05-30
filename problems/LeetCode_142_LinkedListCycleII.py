# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        if not head:
          return None

        slow, fast = head, head
        while True:
          if not fast or not fast.next:
            return None
          slow = slow.next
          fast = fast.next.next
          if slow is fast:
            break

        second = head
        while slow != second:
          slow = slow.next
          second = second.next
        return slow