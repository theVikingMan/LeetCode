def reverseList(head):
  prev, curr = None, head # curr points to start of reverse list

  while curr:
    after = curr.next
    curr.next = prev
    prev = curr
    curr = after

  return prev # prev will be the only non-null pointer which is the new head
  # Interesting -> If no head node is given, prev will be None which is correct output