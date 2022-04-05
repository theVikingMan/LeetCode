def combinationSum3(k, n):
    # Constraints: 1. subset have to be length k and total equals target
    #              2. No duplicate combinations
    #              3. range is 1 - 9 for each num
    #              4. Answer is a 2-D array

    result = []
    subset = []
    topBound = min(n, 10)

    def backtracking(idx, total):
        if (len(subset) == k) and (total == n):
            result.append(subset[::])
            return
        if total > n:
            return

        for j in range(idx, topBound):
            subset.append(j)
            backtracking(j+1, total + j)
            subset.pop()

    backtracking(1, 0)
    return result

print(combinationSum3(2, 4))