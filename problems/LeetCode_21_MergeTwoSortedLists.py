class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      if l1 is None:
          return l2
      elif l2 is None:
          return l1
      elif l1.val < l2.val:
          l1.next = self.mergeTwoLists(l1.next, l2)
          return l1
      else:
          l2.next = self.mergeTwoLists(l1, l2.next)
          return l2

      # dummy = temp = ListNode(0)
      # while l1 and l2:
      #     if l1.val < l2.val:
      #         temp.next = l1
      #         l1 = l1.next
      #     else:
      #         temp.next = l2
      #         l2 = l2.next
      #     temp = temp.next
      # temp.next = l1 or l2
      # return dummy.next