import collections

# --------------- Recursively --------------- #

def maxDepth(root):
    if not root: # leaf node, no depth added
        return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) # +1 depth if node exists

# --------------- Iteratively --------------- #

def maxDepth(root):
    res = 0
    q = collections.deque([root])

    while q:
      res += 1
      for _ in range(len(q)):
        node = q.popleft()
        if node:
          q.append(node.left)
          q.append(node.right)
    return res - 1