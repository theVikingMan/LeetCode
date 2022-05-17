import collections

def solution(rooms):
  ROWS, COLS = len(rooms), len(rooms[0])
  g = collections.deque()
  visit = set() # do not want to revist the same cell twice. If already visited, then it has the min dist to a gate

  def addRoom(r, c):
    if (r < 0 or c < 0 or r == ROWS or c == COLS or # base case of in bounds, not a wall or not visited
       (r, c) in visit or rooms[r][c] == -1):
      return
    visit.add((r,c))
    g.append((r,c))

  # Find all the gates in the matrix that we will initially run BFS on
  for r in range(ROWS):
      for c in range(COLS):
          if rooms[r][c] == 0:
              g.append([r, c])
              visit.add((r, c))
  dist = 0

  while g:
    for _ in range(len(g)): # iterate over the entire current layer of the queue
      r, c = g.popleft()
      rooms[r][c] = dist # mark that as the current distance
      # check all neighbors with a helper function
      addRoom(r + 1, c)
      addRoom(r - 1, c)
      addRoom(r, c - 1)
      addRoom(r, c + 1)
    dist += 1 # increment distance which will then update the valid cell values on the next iteration over the new level

print(solution([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]))
print(solution([[-1]]))