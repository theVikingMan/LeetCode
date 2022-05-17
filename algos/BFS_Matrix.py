import collections

def orangesRotting(grid):
    q = collections.deque()
    time, fresh = 0, 0 # how much time has passed and how many fresh oranges we have
    ROWS, COLS = len(grid),len(grid[0])

    # prework with multiple operations running
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1: # counting number of fresh oranges
                fresh += 1
            if grid[r][c] == 2: # Identify all rotting oranges in order to run multi source BFS
                q.append([r, c])

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while q and fresh > 0: # while we can still run BFS with both rotting and fresh oranges
        for _ in range(len(q)): # Pop everysingle orange and look for adj oranges
            r, c = q.popleft() # mark that we are checking this rotten location
            for dr, dc in directions: # for each direction that we can travel
                row, col = dr + r, dc + c # create the new coordinate as we loop over the directions
                if (row < 0 or col < 0 or # base cases of when to not run BFS
                    row == ROWS or col == COLS or
                    grid[row][col] != 1):
                    continue
                grid[row][col] = 2
                q.append([row, col])
                fresh -= 1
        time += 1
    return time if fresh == 0 else -1