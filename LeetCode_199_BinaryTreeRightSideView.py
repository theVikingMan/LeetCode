# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rightSideView(self, root):
      # base case of nothing given
        if not root:
            return []
        left = self.rightSideView(root.left)
        right = self.rightSideView(root.right)
        return [root.val] + right + left[len(right):]