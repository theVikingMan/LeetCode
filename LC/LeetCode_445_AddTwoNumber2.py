class Solution(object):
    def addTwoNumbers(self, l1, l2):
      s1, s2 = [], []
      while l1:
        s1.append(l1.val)
        l1 = l1.next
      while l2:
        s2.append(l2.val)
        l2 = l2.next

      ones, carry = 0, 0
      res = None

      while s1 or s2 or carry:
        val1 = s1.pop() if s1 else 0
        val2 = s2.pop() if s2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        ones = total % 10

        newHead = ListNode(ones, res)
        res = newHead
      return res


# ---------- Alt way --------- #

class Solution(object):
    def addTwoNumbers(self, l1, l2):
      l1 = self.reverse(l1)
      l2 = self.reverse(l2)

      tens = one = 0
      res = dummy = ListNode(0)

      while l1 or l2 or tens:
        l1Val = l1.val if l1 else 0
        l2Val = l2.val if l2 else 0

        combine = l1Val + l2Val + tens
        ones = combine % 10
        tens = combine // 10

        dummy.next = ListNode(ones)

        dummy = dummy.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

      return self.reverse(res.next)

    def reverse(self, head):
      prev = None
      while head:
        after = head.next
        head.next = prev
        prev = head
        head = after
      return prev
