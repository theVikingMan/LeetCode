def pruneTree(root):
  def isValid(node):
    if not node:
      return False

    left = isValid(node.left)
    right = isValid(node.right)

    if not left:
      node.left = None
    if not right:
      node.right = None

    return node.val or node.right or node.left

  return root if isValid(root) else None