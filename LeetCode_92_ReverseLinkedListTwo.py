# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Create dummy variables to return at the end the modified list
        dummy = ListNode(0)
        dummy.next = head

        # sets up the loop to go until we find the left node to not modify (left_prev) and
        # the start of the nodes we will reverse (curr)
        left_prev, curr = dummy, head
        for _ in range(left - 1):
            left_prev, curr = curr, curr.next

        # Classic reverse linked list BUT for the range of nodes
        # in the range -> +1 because we need that end node that will not be modified
        prev = None
        for _ in range(right - left + 1):
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next

        # Set the initial left node to point to the end node
        # REMEMBER that the start node is still pointing to its original next node
        left_prev.next.next = curr
        # set the initial left node now to the end of the desired range
        left_prev.next = prev

        return dummy.next