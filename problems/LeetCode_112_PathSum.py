import collections

# FOR BOTH
# T: O(n) -> Have to look at possibly all node
# S: O(n) worst case if unbalanced tree, O(log(n)) best case if balanced

# ------------------- Recursively ------------------- #

def hasPathSum(root, sum):
    if not root:  # Base case that null is initially given
        return False

    sum -= root.val # converge the sum onto 0
    if not root.left and not root.right: # if leaf, check if valid answer
        return sum == 0
    return hasPathSum(root.left, sum) or hasPathSum(root.right, sum) # check both subtrees


# ------------------- Iteratively ------------------- #

def hasPathSum(root, targetSum):
    if not root:
      return False
    q = collections.deque([(root, root.val)])

    while q:
      for _ in range(len(q)):
        node, currSum = q.popleft()
        if currSum == targetSum and not node.left and not node.right:
          return True
        if node:
          if node.left:
            q.append((node.left, currSum + node.left.val))
          if node.right:
            q.append((node.right, currSum + node.right.val))
    return False