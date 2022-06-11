# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def maxPathSum(self, root):
    res = [root.val] # keep res as an array so we can update in recursion stack

    def dfs(node):
      if not node: # a Null node has no value to add
        return 0 # give back zero

      leftMax = dfs(node.left) # get left max possibilities WITHOUT SPLITTING
      rightMax = dfs(node.right) # get right max possibilities WITHOUT SPLITTING
      leftMax = max(leftMax, 0) # 0 is if we dont want to include childrent
      rightMax = max(rightMax, 0) # 0 is if we dont want to include childrent

      # possible result if we split. Splitting means no inclusion of parent vals
      res[0] = max(res[0], node.val + leftMax + rightMax)
      # possible result of not splitting, including parent values
      return node.val + max(leftMax, rightMax)

    return max(dfs(root), res[0])