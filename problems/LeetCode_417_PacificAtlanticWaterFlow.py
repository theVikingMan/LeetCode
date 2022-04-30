def pacificAtlantic(heights):
    # Dimensions of the grid
    ROWS, COLS = len(heights), len(heights[0])
    # maintain hash sets for spots that can reach pacific and / or atlantic side
    pac, atl = set(), set()

    def dfs(r, c, visit, prevHeight):
        # Base case -> any case that might mean we CAN'T find a valid path
        if ((r,c) in visit or
            r < 0 or c < 0 or r == ROWS or c == COLS or
            heights[r][c] < prevHeight):
            return
        # marking which spots can reach either ocean
        visit.add((r,c))
        # run dfs on all 4 neighor LIKE WORD SEARCH
        dfs(r + 1, c, visit, heights[r][c])
        dfs(r - 1, c, visit, heights[r][c])
        dfs(r, c + 1, visit, heights[r][c])
        dfs(r, c - 1, visit, heights[r][c])
    # go thorugh every position in the first and last row
    for c in range(COLS):
        # run a DFS on all of the top row spots as we know they can reach the Pacific ocean
            # 0 is the first row and c will travese across. Last item is the previous spot's height
        dfs(0, c, pac, heights[0][c])
        # run a DFS on all of the bottom row spots as we know they can reach the Atlantic ocean
        dfs(ROWS -1, c, atl, heights[ROWS - 1][c])

    # go through every position in the first and last column
    for r in range(ROWS):
        # Run DFS for all positions on the left most column
        dfs(r, 0, pac, heights[r][0])
        # Run DFS for all positiions on the right most column
        dfs(r, COLS - 1, atl, heights[r][COLS -1])

    # result variable
    result = []
    # Go through every coordinate in the grid to see whether it can reach both oceans
    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) in pac and (r, c) in atl:
                result.append([r, c])

    return result

print(pacificAtlantic([[1,2,2,3,5],
                        [3,2,3,4,4],
                        [2,4,5,3,1],
                        [6,7,1,4,5],
                        [5,1,1,2,4]]))