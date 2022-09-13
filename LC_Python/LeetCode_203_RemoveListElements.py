# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        if not head:
            return None

        before = dummy
        after = dummy.next

        while after:
            if after.val != val:
                before.next = after
                before = before.next
            after = after.next

        before.next = None

        return dummy.next