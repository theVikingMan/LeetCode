# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        self.dfs(root)
        return self.diameter

    def dfs(self, node):
        if not node:
            return 0
        left_side = self.dfs(node.left)
        right_side = self.dfs(node.right)
        self.diameter = max(self.diameter, left_side + right_side)
        return 1 + max(left_side, right_side)