import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def sumNumbers(self, root):
    q = collections.deque([[root, root.val]]) # initialize q with root
    res = 0

    while q:
      for _ in range(len(q)):
        node, total = q.popleft()
        if node:
          if not node.left and not node.right: # base case of lead node
            res += total # finally add to result
            continue # move on to the next leaf node if there are any
          newTotal = total * 10 # keep shifting tens place till leaf
          if node.left:
            q.append([node.left, newTotal + node.left.val]) # add node value in append
          if node.right:
            q.append([node.right, newTotal + node.right.val]) # add node value in append
    return res