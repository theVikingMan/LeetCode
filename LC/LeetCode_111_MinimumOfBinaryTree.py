
# -------------- Recursive option A ----------- #

def minDepth(root):
  if not root:
    return 0

  def dfs(node):
    if not node:
      return float('inf')
    if not node.left and not node.right:
      return 1
    return 1 + min(dfs(node.left), dfs(node.right))

  return dfs(root)

# -------------- Recursive option B ----------- #

def minDepth(self, root):
    def recurse(root):
        if root.left and root.right:
            return min(self.minDepth(root.left) + 1, (self.minDepth(root.right) + 1))
        if root.left and not root.right:
            return self.minDepth(root.left) + 1
        if root.right and not root.left:
            return self.minDepth(root.right) + 1
        if not root.left and not root.right:
            return 1
    return recurse(root) if root else 0

