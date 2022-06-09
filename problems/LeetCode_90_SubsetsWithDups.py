def subsetsWithDup(nums):

    result, subset = [], []
    nums.sort() # Have to sort for duplicate detection
    lenNums = len(nums) # storing repeated work

    def backtrack(subset, i):
        if i == lenNums: # reached the end of the original array with all possibilities
            result.append(subset[::]) # [::] makes a copy and we append to result array
            return

        # All subsets that include nums[i]
        subset.append(nums[i])
        backtrack(subset, i + 1)

        # All subsets that do not include nums[i]
        subset.pop() # clean up which is called BACKTRACKING so we can look at other vailable solutions
        while i + 1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        backtrack(subset, i + 1)

    backtrack(subset, 0)
    return result

print(subsetsWithDup([1, 2, 2, 3]))