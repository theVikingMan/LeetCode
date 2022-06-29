
def pathSum(root, targetSum):
    if not root: # check edge case of nothing given
      return 0
    count = [0] # array with one value to access in DFS. Result variable
    prefixSums = { 0 : 1 } # track with prefix sums seen and num of times

    def dfs(node, currTotal):
      if not node: # reached the end
        return

      diff = currTotal - targetSum # what do we need to have seen
      count[0] += prefixSums.get(diff, 0) # add how many time we've seen it
      prefixSums[currTotal] = 1 + prefixSums.get(currTotal, 0) # say we have seen it

      if node.left:
        dfs(node.left, currTotal + node.left.val)
      if node.right:
        dfs(node.right, currTotal + node.right.val)
      prefixSums[currTotal] -= 1 # clean up so one side doesnt count the other
                                 # think about a leaf node on the left side, no right so we clean up

    dfs(root, root.val)
    return count[0]