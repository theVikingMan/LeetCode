# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
      # Check if both are null first, meaning that everything else
      # was the same up to that point
        if not p and not q:
            return True
      # or works here bc it exposes one or the other is null given we
      # checked prior that both might be null
      # If order is switched, a end node for BOTH trees will set the False off
        if (not p or not q) or (p.val != q.val):
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)