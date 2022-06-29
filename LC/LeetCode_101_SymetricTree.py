
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# -------------- Recursive Option #1 -------------- #

class Solution:
  def isSymmetric(self, root):
    if not root:
      return True

    def dfs(l, r):
      if not l and not r:
        return True
      if (not l or not r) or l.val != r.val:
        return False
      return dfs(l.left, r.right) and dfs(l.right, r.left)

    return dfs(root.left, root.right)

# -------------- Recursive Option #2 -------------- #

class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        if left.val == right.val:
            outPair = self.isMirror(left.left, right.right)
            inPiar = self.isMirror(left.right, right.left)
            return outPair and inPiar
        else:
            return False


