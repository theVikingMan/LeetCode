# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
      # Check base case of no root initially given
        if not root:
            return []
        ans = []
        # Begin the stack off at the root
        stack = [[root]]

        while stack:
            # check the recent level
            level = stack.pop()
            # Get all the data for that level in an array format
            level_data = [node.val for node in level]

            # append that array to the ans as each new level
            # will be tacked on TO THE BACK WITH APPEND
            ans.append(level_data)

            # Gather the next level
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            # Data validation for each level
            if len(next_level) > 0:
                stack.append(next_level)

        return ans

#      RECURSIVELY
#         ordering = {}
#         output = []

#         def dfs(node, h):
#             if not node:
#                 return
#             if h not in ordering:
#                 ordering[h] = []
#             ordering[h].append(node.val)
#             dfs(node.left, h + 1)
#             dfs(node.right, h + 1)

#         dfs(root, 0)

#         for i in range(len(ordering)):
#             output.append(ordering[i])

#         return output

