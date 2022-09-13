def lowestCommonAncestor(self, p, q):
  pMap = set()

  curr = p
  while curr:
    pMap.add(curr.val)
    curr = curr.parent

  curr = q
  while curr:
    if curr.val in pMap:
      return curr
    curr = curr.parent