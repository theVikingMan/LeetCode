import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def sumNumbers(self, root):
    q = collections.deque([[root, root.val]])
    res = 0

    while q:
      for _ in range(len(q)):
        node, total = q.popleft()
        if node:
          if not node.left and not node.right:
            res += total
            continue
          newTotal = total * 10
          if node.left:
            q.append([node.left, newTotal + node.left.val])
          if node.right:
            q.append([node.right, newTotal + node.right.val])
    return res