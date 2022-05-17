def numIslands(grid):
    if len(grid) < 1 or len(grid[0]) < 1:
        return 0
    res = 0
    ROWS, COLS = len(grid), len(grid[0])
    visited = set()

    def search(r, c):
        if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visited or grid[r][c] == "0":
            return
        visited.add((r,c))
        search(r + 1, c)
        search(r - 1, c)
        search(r, c + 1)
        search(r, c - 1)
        return

    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) not in visited and grid[r][c] == "1":
                res += 1
                search(r, c)
    return res


