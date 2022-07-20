import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def levelOrder(self, root):
    if not root:
      return res

    q = collections.deque([root])
    res = []

    while q:
      level = []
      for _ in range(len(q)):
        node = q.popleft()
        level.append(node.val)
        if node.left:
          q.append(node.left)
        if node.right:
          q.append(node.right)
      if level:
        res.append(level)
    return res

# ----------- RECURSIVELY ----------- #

# def levelOrder(root):
#   res = []

#   def helper(node, level):
#     if not node:
#       return
#     if len(res) < level:
#       res.append([node.val])
#     else:
#       res[level-1].append(node.val)

#     helper(node.left, level+1)
#     helper(node.right, level+1)

#   helper(root, 1)
#   return res

