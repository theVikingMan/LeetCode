# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ----------- Recursive ----------- #

class Solution:
    def inorderTraversal(self, root):
        res = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res

# ----------- Iterative ----------- #

class Solution:
  def inorderTraversal(self, root):
    if not root:
      return root
    stack, res = [], []

    while True:
      while root:
        stack.append(root)
        root = root.left
      if not stack:
        return res
      node = stack.pop()
      res.append(node.val)
      root = node.right