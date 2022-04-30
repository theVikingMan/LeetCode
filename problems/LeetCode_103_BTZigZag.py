import collections
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        # Create queue that we can take from the front (i.e., pop left)
        queue = collections.deque([root])
        # Create output variable that will be a 2-D array
        output = []

        while queue:
            # array to append to result
            to_add = []
            # Loop through all the nodes in that most recent level
            for _ in range(len(queue)):
                # FIFO
                node = queue.popleft()
                if node:
                    to_add.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if to_add:
                # Heres the magic, reverse if odd row
                output.append(to_add if len(output) % 2 == 0 else to_add[::-1])
        return output