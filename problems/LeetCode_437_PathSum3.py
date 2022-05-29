import collections

def pathSum(root, targetSum):
    def dfs(sumHash, prefixSum, node):
        if not node:
            return 0

        prefixSum += node.val # Sum of current path
        path = sumHash[prefixSum - targetSum] # number of paths that ends at current node
        sumHash[prefixSum] += 1  # add currentSum to prefixSum Hash

        # traverse left and right of tree
        path += dfs(sumHash, prefixSum, node.left) + dfs(sumHash, prefixSum, node.right)

        sumHash[prefixSum] -= 1 # remove currentSum from prefixSum Hash

        return path

    # DFS, initialize sumHash with prefix sum of 0, occurring once
    return dfs(collections.defaultdict(int, {0: 1}), 0, root)