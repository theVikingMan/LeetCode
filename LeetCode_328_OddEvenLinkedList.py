# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head):
        if not head:
            return head
        odd, even = head, head.next
        firstEven = head.next
        dummy = ListNode()
        dummy.next = head


        while even and even.next:
            odd.next = even.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = firstEven
        return dummy.next
