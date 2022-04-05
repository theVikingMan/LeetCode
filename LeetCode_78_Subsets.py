 # def subsets(nums):
    # result = [[]]
    # for num in nums:
    #     for i in range(len(result)):
    #         result.append(result[i] + [num])
    # return resuålt


def subsets(nums):
    output = []
    subset = []

    def dfs(i):
        if i >= len(nums):
            output.append(subset.copy())
            return
        # Decision 1: include the num BUT have to move on
        subset.append(nums[i])
        dfs(i + 1)
        # Decision 2: DON'T include the num BUT have to move on
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return output

print(subsets([1, 2, 3]))
