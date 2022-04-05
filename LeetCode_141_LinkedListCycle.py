# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow = fast = head
        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return False
            if slow is fast:
                return True
        return False