# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def pseudoPalindromicPaths (self, root):
    def dfs(node, count):
      if not node:
        return 0
      count[node.val] = 1 + count.get(node.val, 0)
      if count[node.val] == 2:
        del count[node.val]
      if not node.left and not node.right:
        return 1 if len(count) < 2 else 0
      # need copy to prevent changes spilling over into other call stacks
      return dfs(node.left, count.copy()) + dfs(node.right, count.copy())

    return dfs(root, {})