def middleNode(head):
    if not head or not head.next:
      return head
    slow, fast = head, head
    while fast and fast.next:
      slow, fast = slow.next, fast.next.next
    return slow
