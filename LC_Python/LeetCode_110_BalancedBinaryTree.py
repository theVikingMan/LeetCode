# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        return self.getHeight(root) != -1

    def getHeight(self, node):
        if not node:
            return 0

        left = self.getHeight(node.left)
        right = self.getHeight(node.right)
        # Need to bubble up if any sub trees are unbalanced
        # -1 instead of returning false if the diff is more than 1.
        # Returning False if the diff is under 1 would be tricked if tree is
        # only balanced at the root node, not subs
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)