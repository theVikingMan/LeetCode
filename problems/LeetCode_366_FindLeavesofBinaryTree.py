import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def findLeaves(self, root):
      res = []

      def bfs(node):
        if not node: # reach an end, return None
          return None
        if not node.left and not node.right: # hit a leaf
          res[-1].append(node.val) # append to current level in res
          return None # mark it as none which will turn the children of parent into Nones
        node.left = bfs(node.left) # if a leaf was to left, it will now be None
        node.right = bfs(node.right) # allowing for the next level appending to happen
        return node # return back the node to the original tree
      while root: # while there are still leafs to look at
        res.append([]) # append for new round of leafs
        root = bfs(root) # send tree back through to harvest leafs
      return res