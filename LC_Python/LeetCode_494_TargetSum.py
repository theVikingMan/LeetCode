def findTargetSumWays(nums, target):
    dp = {} # (index, total) -> # of ways

    def dfs(i, total):
        if i == len(nums): # add if we have hit the target or do nothing if we have not hit target
            return 1 if total == target else 0
        if (i, total) in dp: # check if calc already done at that position with same decisions made
            return dp[(i, total)]

        # store the results of choosing to add / subtract the element
        dp[(i, total)] = (dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i]))
        return dp[(i, total)]

    return dfs(0, 0)

print(findTargetSumWays([1, 1, 1, 1], 2))

# DFS implementation with pruning.

# T: O(n * t) -> where t is all sums of the array
# S: O(n * t) -> where n is the depth of the recusion tree