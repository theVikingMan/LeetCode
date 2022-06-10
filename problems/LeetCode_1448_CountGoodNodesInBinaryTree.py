class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def goodNodes(root):
  def dfs(node, high, res):
    if not node:
      return 0
    if node.val >= high:
      high = max(high, node.val)
      return 1 + dfs(node.left, high, res) + dfs(node.right, high, res)
    high = max(high, node.val)
    return dfs(node.left, high, res) + dfs(node.right, high, res)
  return dfs(root, float('-inf'), 0)

# ----------- Same solution, Better written ----------- #

def goodNodes(root):
  def dfs(node, high, res):
    if not node:
      return 0
    res = 1 if node.val >= high else 0
    high = max(high, node.val)
    res += dfs(node.left, high, res)
    res += dfs(node.right, high, res)
    return res
  return dfs(root, float('-inf'), 0)