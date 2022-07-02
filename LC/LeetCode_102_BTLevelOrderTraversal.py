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
# class Solution:
#     def levelOrder(self, root):
#         ordering = {}
#         output = []

#         def dfs(node, h):
#             if not node:
#                 return
#             if h not in ordering:
#                 ordering[h] = []
#             ordering[h].append(node.val)
#             dfs(node.left, h + 1)
#             dfs(node.right, h + 1)

#         dfs(root, 0)

#         for i in range(len(ordering)):
#             output.append(ordering[i])

#         return output

