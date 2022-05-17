import collections

# Iteratively
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

# Helper funciton used (think about what variables you are accessing with the iterations)
def wallsAndGates(rooms):
    ROWS, COLS = len(rooms), len(rooms[0])
    g = collections.deque()
    visit = set() # do not want to revist the same cell twice. If already visited, then it has the min dist to a gate

    # helper function to avoid varbose amount of code
    def addRoom(r, c):
        if (r < 0 or c < 0 or r == ROWS or c == COLS or
        (r, c) in visit or rooms[r][c] == -1): # in bounds, havent seen and are not barriers
            return
        visit.add((r,c))
        g.append((r,c))

    # find all the initial starting points which are the gates to run BFS
    for r in range(ROWS):
        for c in range(COLS):
            if rooms[r][c] == 0:
                g.append([r, c])
                visit.add((r, c))
    dist = 0
    while g:
        for _ in range(len(g)):
            r, c = g.popleft()
            rooms[r][c] = dist
            addRoom(r + 1, c)
            addRoom(r - 1, c)
            addRoom(r, c - 1)
            addRoom(r, c + 1)