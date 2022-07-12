def reverseList(head):
  if not head: # check if nothing was given as an input
    return head # head will be empty if so

  prev, curr = None, head # curr points to start of reverse list

  while curr:
    after = curr.next
    curr.next = prev
    prev = curr
    curr = after

  return prev # prev will be the only non-null pointer which is the new head