import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def widthOfBinaryTree(root):
  res = 0
  queue = collections.deque([[root, 1, 1]])

  while queue:
    minNode, maxNode = float('inf'), float('-inf')
    for _ in range(len(queue)):
      node, level, number = queue.popleft()
      minNode = min(minNode, number)
      maxNode = max(maxNode, number)
      if node.left:
        queue.append([node.left, level + 1, number * 2])
      if node.right:
        queue.append([node.right, level + 1, (number * 2) + 1])
    res = max(res, (maxNode - minNode) + 1)
  return res