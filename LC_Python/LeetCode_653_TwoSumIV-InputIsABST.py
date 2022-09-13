# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findTarget(self, root, k):
  seen = set()

  def dfs(node):
    if not node:
      return False
    target = k - node.val
    if target in seen:
      return True
    else:
      seen.add(node.val)
      return dfs(node.left) or dfs(node.right)

  return dfs(root)