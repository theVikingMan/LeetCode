def pacificAtlantic(heights):
    ROWS, COLS = len(heights), len(heights[0]) # Dimensions of the grid
    pac, atl = set(), set() # maintain hash sets for spots that can reach pacific and / or atlantic side

    def dfs(r, c, visit, prevHeight):
        if ((r,c) in visit or
            r < 0 or c < 0 or r == ROWS or c == COLS or
            heights[r][c] < prevHeight): # Base case -> any case that might mean we CAN'T find a valid path
            return
        visit.add((r,c)) # marking which spots can reach either ocean, idp. of which set()
        # run dfs on all 4 neighor LIKE WORD SEARCH
        dfs(r + 1, c, visit, heights[r][c])
        dfs(r - 1, c, visit, heights[r][c])
        dfs(r, c + 1, visit, heights[r][c])
        dfs(r, c - 1, visit, heights[r][c])

    for c in range(COLS): # go through every position in the first and last row
        dfs(0, c, pac, heights[0][c]) # run a DFS on all of the top row spots as we know they can reach the Pacific ocean
        dfs(ROWS -1, c, atl, heights[ROWS - 1][c]) # run a DFS on all of the bottom row spots as we know they can reach the Atlantic ocean

    for r in range(ROWS):
        dfs(r, 0, pac, heights[r][0]) # Run DFS for all positions on the left most column
        dfs(r, COLS - 1, atl, heights[r][COLS -1]) # Run DFS for all positiions on the right most column

    result = []
    for r in range(ROWS): # Go through every coordinate in the grid to see whether it can reach both oceans
        for c in range(COLS):
            if (r, c) in pac and (r, c) in atl:
                result.append([r, c])

    return result

print(pacificAtlantic([[1,2,2,3,5],
                        [3,2,3,4,4],
                        [2,4,5,3,1],
                        [6,7,1,4,5],
                        [5,1,1,2,4]]))