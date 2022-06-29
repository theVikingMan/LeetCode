# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ------------- Smart Recursive Way -------------

def rangeSumBST(root, low, high):
  if not root:
    return 0
  if low <= root.val <= high:
    return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
  if root.val < low:
    return self.rangeSumBST(root.right, low, high)
  elif root.val > high:
    return self.rangeSumBST(root.left, low, high)


# ------------- Slow Recursive Way -------------

def rangeSumBST(root, low, high):
    arr = []

    def dfs(node):
      if not node:
        return
      if low <= node.val <= high:
        arr.append(node.val)
      dfs(node.left)
      dfs(node.right)

    dfs(root)
    return sum(arr)