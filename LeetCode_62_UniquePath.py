def uniquePaths(m, n):
# I - The demensions of the board
#   - Only move d or r
# O - Ways of reaching the cordinate (m, n)
# E - 1 x 1 grid

    row = [1] * n
    for i in range(m - 1):
        newRow = [1] * n
        for j in range(n - 2, -1, -1):
            newRow[j] = row[j] + newRow[j+1]
        row = newRow
    return row[0]


print(uniquePaths(2, 2))


    # BFS WITH MEMOIZATION
    # dp = {}
    # def dfs(d, r):
    #     if (d, r) in dp:
    #         return dp[(d, r)]
    #     if d == 0 and r == 0:
    #         return 1
    #     if d < 0 or r < 0:
    #         return 0
    #     dp[(d, r)] = dfs(d - 1, r) + dfs(d, r - 1)

    #     return dp[(d,r)]

    # dfs(m-1, n-1)
    # return dp[(m-1, n-1)]