import collections

def verticalOrder(root):
  l, r = [], []
  q = collections.deque([[root, 0]])

  while q:
    for _ in range(len(q)):
      node, col = q.popleft()
      if node:
        if col < 0:
          l[abs(col) - 1].append(node.val) if len(l) >= abs(col) else l.append([node.val])
        else:
          r[col].append(node.val) if len(r) >= col+1 else r.append([node.val])
        if node.left:
          q.append([node.left, col - 1])
        if node.right:
          q.append([node.right, col + 1])
  return l[::-1] + r