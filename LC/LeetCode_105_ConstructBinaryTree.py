# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution(object):
  def buildTree(self, preorder, inorder):
    # Base case: Nothing is given initially
    if not preorder or not inorder:
        return None
    # Create the root node
    root = TreeNode(preorder[0])
    # Find position of that root node in the inorder
    mid = inorder.index(preorder[0]) # Preorder: 1st value is the root of the current tree
    root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
    root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

    return root

# preorder = [3, 9,5,6, 20,15,7], inorder = [5,9,6, 3, 15,20,7]
