import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderBottom(root):
  res = []
  q = collections.deque([root])

  while q:
    level = []
    for _ in range(len(q)):
      node = q.popleft()
      if node:
        level.append(node.val)
        q.append(node.left)
        q.append(node.right)
    if level:
      res.insert(0, level)
  return res