def combinationSum3(k, n):
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