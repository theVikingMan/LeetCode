# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# ----------- 2-Pointers (optimal) -------- #

def getIntersectionNode(headA, headB):
    l1, l2 = headA, headB
    # Intuition: Both pointers, if they have common nodes, will travel the same
      # length if they travese both LL (l1 = 4, l2 = 3, total 7 moves till clash)
    while l1 != l2: # either equal eachother or both will be Null
        if l1:
            l1 = l1.next
        else: # if reached null, set it to the other head
            l1 = headB
        if l2:
            l2 = l2.next
        else: # if reached null, set it to the other head
            l2 = headA
    return l1 # will be the common node or Null

# T: O(n + m) --> n is length of headA, m is length of headB
# S: O(1) --> nothing is stored besides 2 pointers

# ----------- Hash set (valid) -------- #

def getIntersectionNode(headA, headB):
  dic = set()
  curr = headA
  while curr:
    dic.add(curr)
    curr = curr.next

  curr = headB
  while curr:
    if curr in dic:
      return curr
    curr = curr.next
  return None

# T: O(n + m) --> n is length of headA, m is length of headB
# S: O(n) --> n is length of headA. Only need to store one LL