# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
    seenNone = False

    q = collections.deque([root])

    while q:
      if seenNone:
        return not any(q)

      for _ in range(len(q)):
        node = q.popleft()
        if not node: # first Null node
          seenNone = True
        else: # valid node
          if seenNone:
            return False
          else:
            q.append(node.left)
            q.append(node.right)
    return True