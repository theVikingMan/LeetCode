def subsetsWithDup(nums):

    result = []
    subset = []
    nums.sort()
    lenNums = len(nums)

    def backtrack(subset, i):
        if i == lenNums:
            result.append(subset[::])
            return
        # All subsets that include nums[i]
        subset.append(nums[i])
        backtrack(subset, i + 1)
        subset.pop()

        # All subsets that do not include nums[i]
        while i + 1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        backtrack(subset, i + 1)


    backtrack(subset, 0)
    return result

print(subsetsWithDup([1, 2, 2, 3]))