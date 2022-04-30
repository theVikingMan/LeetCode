# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        infinity, negInfinity = float('inf'), float('-inf')

        def helper(node, lower, upper):
            # If we reach the end of a tree branch
            if not node:
                return True
            # Check if our node is in the in the right spot depending on the side
            if (lower < node.val < upper):
                return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)
            else:
                return False

        return helper(root, negInfinity, infinity)