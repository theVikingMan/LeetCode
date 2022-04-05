def numIslands(grid):
    # Base case: check if edge case that we are given nothing
    if len(grid) < 1:
        return 0
    # Set usual variables for grid problems
    ROWS, COLS = len(grid), len(grid[0])
    # visited set to check if we have already seen the island
    # which we will add during our DFS
    visited = set()

    def dfs(r, c):
        # Base case: Check if we are out bounds
        # OR that its water or that we have DFS'd on it before
        if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
            grid[r][c] == "0" or (r, c) in visited):
            return

        # say we have seen it which will be useful for checking DFS and
        # if it is a new island
        visited.add((r,c))
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    result = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "1" and (r,c) not in visited:
                result += 1
                dfs(r, c)

    return result

print(numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))