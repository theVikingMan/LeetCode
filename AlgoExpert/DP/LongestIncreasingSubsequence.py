def longestIncreasingSubsequence(array):
    res = []
    resL, resIdx = 0, 0
    dp = [1 for _ in range(len(array))]
    path = [i for i in range(len(array))]

    for i in range(len(array) - 1, -1, -1):
        for j in range(i+1, len(array)):
            if array[j] > array[i]:
                if 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
                    path[i] = j
                if dp[i] > resL:
                    resL = dp[i]
                    resIdx = i
    c = resIdx
    while True:
        res.append(array[c])
        if path[c] == c:
            break
        c = path[c]

    return res

print(longestIncreasingSubsequence([5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]))