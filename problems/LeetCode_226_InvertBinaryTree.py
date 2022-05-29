import collections
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        # Base case: if we are given no root at the beginning
        # OR that we ahve reached the end
        if not root:
            return
        # holder for one of the nodes as we will modify it but need a version that is
        # unmodified
        temp = root.right
        root.right = root.left
        root.left = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# --------------- Iteratively --------------- #

def invertTree(root):
    queue = collections.deque([(root)])
    while queue:
        node = queue.popleft()
        if node:
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)
    return root