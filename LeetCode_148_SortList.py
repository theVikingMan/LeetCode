# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        # Solution --> Split, sort, merge
        # Base case: No node given or just one node
        if not head or not head.next:
            return head

        # Split the list into halfs
        left = head
        # Find the middle node (or kind of the left middle node)
        right = self.getMid(head)
        # Save the beginning of the right side's node
        tmp = right.next
        # Make the cut
        right.next = None
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)

        # once broken down into small bites, they will need to be sorted
        return self.merge(left, right)
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, list1, list2):
        tail = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 or list2
        return dummy.next

