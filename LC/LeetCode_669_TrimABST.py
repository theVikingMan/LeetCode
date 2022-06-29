# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def trimBST(root, low, high):
  if not root: # reached an end of a path
    return None
  # check if cur node val is in our range
  if low <= root.val <= high: # yes -> add it to the new tree -> look both right and left
    tree = TreeNode(root.val)
    tree.left = trimBST(root.left, low, high)
    tree.right = trimBST(root.right, low, high)
    return tree
  # not a valid node
  elif root.val < low: # if less than -> go right till none
    return trimBST(root.right, low, high)
  elif root.val > high: # if more than -> go left till none
    return trimBST(root.left, low, high)