# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # if it is not found in a side, then root will be None and will not execute the output logic
        # else (basically) we found the node in the side we are checking
        if not root or p is root or q is root:
            return root
        # Check if EITHER target node exists on EITHER side
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        # if both returned a none Null node (returned back their "root"), then we have the result
        if l and r:
            return root
        else:
            #situation where the starting node has only one side or
            return l if l else r