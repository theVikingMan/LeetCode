
def pathSum(root, targetSum):
    if not root:
      return 0
    count = [0]
    prefixSums = { 0 : 1 }

    def dfs(node, currTotal):
      if not node:
        return

      diff = currTotal - targetSum
      count[0] += prefixSums.get(diff, 0)
      prefixSums[currTotal] = 1 + prefixSums.get(currTotal, 0)

      if node.left:
        dfs(node.left, currTotal + node.left.val)
      if node.right:
        dfs(node.right, currTotal + node.right.val)
      prefixSums[currTotal] -= 1 # Have to clean up for that path as other paths
                                 # dont have access to that sum
    dfs(root, root.val)
    return count[0]