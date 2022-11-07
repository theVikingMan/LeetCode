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
    result = []
    queue = collections.deque([root])

    while queue:
      queueLen = len(queue)
      rightNode = None
      for _ in range(queueLen):
        node = queue.popleft()
        if node:
          rightNode = node
          queue.append(node.left)
          queue.append(node.right)
      if rightNode:
        result.append(rightNode.val)
    return result