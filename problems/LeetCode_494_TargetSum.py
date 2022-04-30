def findTargetSumWays(nums, target):
    dp = {} # (index, total) -> # of ways

    def dfs(i, total):
        # if we have performed some aciton with all possible nums then
        # add if we have hit the target or do nothing if we have not hit target
        if i == len(nums):
            return 1 if total == target else 0

        # For memoization but if we have already found a way then no
        # need to redo the calculation
        if (i, total) in dp:
            return dp[(i, total)]

        # store the results of choosing to add / subtract the element
        dp[(i, total)] = (dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i]))

        return dp[(i, total)]

    return dfs(0, 0)

print(findTargetSumWays([1, 1, 1, 1], 2))

# DFS implementation with pruning.