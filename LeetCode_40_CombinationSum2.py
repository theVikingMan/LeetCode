def combinationSum2(candidates, target):
    result = []
    subset = []
    # Allows for the while loop to handle duplicates as they are next to eachother
    candidates.sort()

    def backtracking(idx, total):
        # Base case: we have a set of nums that hit the target so add to res
        if total == target:
            result.append(subset[::])
            return

        # We have too many numbers or we have gone over the target
        if idx == len(candidates) or total > target:
            return

        # Decision 1: include the num so add it to temp total and MOVE ONWARDS
        # slight difference from Uno ComboSum per instructions
        subset.append(candidates[idx])
        backtracking(idx + 1, total + candidates[idx])

        # Decision 2: Don't include current num and move on to the next UNIQUE
        # number to then make a dicision on
        subset.pop()

        while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
            idx += 1
        backtracking(idx + 1, total)

    backtracking(0, 0)
    return result

print(combinationSum2([2,5,2,1,2], 5))