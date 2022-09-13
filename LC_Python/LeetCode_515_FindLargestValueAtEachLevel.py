# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution(object):
    def largestValues(self, root):
      if not root:
        return []
      q = collections.deque([root])
      res = []

      while q:
        levelMax = float('-inf')
        for _ in range(len(q)):
          node = q.popleft()
          if node:
            levelMax = max(node.val, levelMax)
            if node.left:
              q.append(node.left)
            if node.right:
              q.append(node.right)
        res.append(levelMax)
      return res

# ------------ Recursively -------------- #

# def largestValues(self, root):
#   if not root:
#     return []

#   res = []

#   def helper(node, level):
#     if not node:
#       return
#     if len(res) == level:
#       res.append(node.val)

#     res[level] = max(res[level], node.val)
#     helper(node.right, level+1)
#     helper(node.left, level+1)
#   helper(root, 0)
#   return res
