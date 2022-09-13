# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        curr = dummy

        carry = 0
        # If we haven't reached the end of our linked lists
        # OR that we had some calc at the end (8 + 3) that is the end of the LL but
        # still need to tack on the carry
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            value = val1 + val2 + carry
            # Gets you the tens place num
            carry = value // 10
            # Gets you the ones place num
            ones = value % 10

            curr.next = ListNode(ones)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next

        return dummy.next
