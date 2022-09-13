# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
  def boundaryOfBinaryTree(self, root):
    def handleLeft(node):
      if not node or (not node.left and not node.right):
        return
      boundry.append(node.val)
      if node.left:
        handleLeft(node.left)
      else:
        handleLeft(node.right)


    def handleRight(node):
      if not node or (not node.left and not node.right):
        return
      if node.right:
        handleRight(node.right)
      else:
        handleRight(node.left)
      boundry.append(node.val)

    def handleLeafs(node):
      if not node:
        return
      handleLeafs(node.left)
      if not node.left and not node.right and node != root:
        boundry.append(node.val)
      handleLeafs(node.right)

    if not root:
      return []

    boundry = [root.val]
    handleLeft(root.left)
    handleLeafs(root)
    handleRight(root.right)
    return boundry