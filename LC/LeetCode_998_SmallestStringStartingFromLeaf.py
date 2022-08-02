# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution(object):
  def smallestFromLeaf(self, root):
    resultSum = 'z' * 26
    q = collections.deque([[root, chr(root.val + ord('a'))]])

    while q:
      node, string = q.popleft()
      correctString = string[::-1]
      if not node.left and not node.right and correctString < resultSum:
        resultSum = correctString

      if node.left:
        q.append([node.left, string + chr(node.left.val + ord('a'))])
      if node.right:
        q.append([node.right, string + chr(node.right.val + ord('a'))])

    return resultSum
