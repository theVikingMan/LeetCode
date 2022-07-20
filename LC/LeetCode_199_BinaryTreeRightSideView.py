import collections
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ------ Recursively ------ #

class Solution(object):
    def rightSideView(self, root):
      # base case of nothing given
        if not root:
            return []
        left = self.rightSideView(root.left)
        right = self.rightSideView(root.right)
        return [root.val] + right + left[len(right):]

# ----- Iteratively ----- #
class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []

        q = collections.deque([root])
        res = []

        while q:
            levLength = len(q)

            for i in range(levLength):
                node = q.popleft()
                if i == levLength - 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res