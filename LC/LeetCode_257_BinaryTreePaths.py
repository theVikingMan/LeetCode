# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def binaryTreePaths(self, root):
    res = []
    if not root:
      return ""

    def dfs(node, temp):
      if not node:
        return
      temp += str(node.val)
      if not node.left and not node.right:
        res.append(temp)
        return
      temp += "->"
      dfs(node.left, temp)
      dfs(node.right, temp)
    dfs(root, "")
    return res