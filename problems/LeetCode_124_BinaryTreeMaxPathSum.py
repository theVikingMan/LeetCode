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
      leftMax = max(leftMax, 0) # 0 -> dont want to include children (0 means nothing is added)
      rightMax = max(rightMax, 0) #  0 -> dont want to include children (0 means nothing is added)

      # possible result if we split. Splitting means no inclusion of parent vals
      res[0] = max(res[0], node.val + leftMax + rightMax)
      # possible result of not splitting, including parent values
      return node.val + max(leftMax, rightMax)

    return max(dfs(root), res[0])

# T: O(n) -> will need to check all nodes at most twice
# S: O(H) -> height of the tree for the call stack, O(log(n)) if balanced so best case