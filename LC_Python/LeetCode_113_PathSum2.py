import collections

# ------------------- Recursively ------------------- #

def pathSum(root, targetSum):
  if not root:
    return root
  output = []

  def helper(node, total, currArray):
      if not node:
          return
      total += node.val
      if total == targetSum and not node.left and not node.right:
          currArray.append(node.val)
          output.append(currArray)
          return

      helper(node.left, total, currArray + [node.val])
      helper(node.right, total , currArray + [node.val])

  helper(root, 0, [])
  return output

# ------------------- Iteratively ------------------- #

def pathSum(root, targetSum):
  if not root:
    return []
  q = collections.deque([(root, targetSum - root.val, [root.val])])
  res = []

  while q:
    for _ in range(len(q)):
      node, curSum, path = q.popleft()
      if not node.left and not node.right and curSum == 0:
        res.append(path)
      if node.left:
        q.append((node.left, curSum - node.left.val, path + [node.left.val]))
      if node.right:
        q.append((node.right, curSum - node.right.val, path + [node.right.val]))

  return res
