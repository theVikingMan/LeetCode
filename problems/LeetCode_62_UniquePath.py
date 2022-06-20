def uniquePaths(m, n):
    row = [1] * n
    for _ in range(m - 1):
        newRow = [1] * n
        for j in range(n - 2, -1, -1):
            newRow[j] = row[j] + newRow[j+1]
        row = newRow
    return row[0]

print(uniquePaths(2, 2))

#  --------- RECURSION WITH MEMOIZATION --------- #

# def uniquePaths(m, n):
#   cache = {} # (r, c) : nums ways
#   visit = set()
#   ROWS, COLS = m, n

#   def dfs(r, c):
#     if (r, c) in cache:
#       return cache[(r, c)]
#     if (r, c) == (m-1, n-1):
#       return 1
#     if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visit:
#       return 0

#     visit.add((r, c))
#     cache[(r, c)] = (dfs(r + 1, c) + dfs(r, c + 1))

#     return cache[(r, c)]

#   return dfs(0, 0)