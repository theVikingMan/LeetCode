# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root):
      def dfs(root): # flatten root tree and return the list tail
        if not root: # edge case of not root given. Standard tree / LL catch
          return None

        leftTail = dfs(root.left)
        rightTail = dfs(root.right)

        if leftTail: # flatten left sub-tree and then insert into right side
          leftTail.right = root.right # take left base node, point to the right side
          root.right = root.left # point root to the new lefttail
          root.left = None # All left pointers should be None

        last = rightTail or leftTail or root # Need to point to the last node (recursively) after each flatten
        return last

      dfs(root) # Only need to modify original tree

# Time: O(n) --> Need to only look at each node once
# Space: O(1) --> In-place modification
