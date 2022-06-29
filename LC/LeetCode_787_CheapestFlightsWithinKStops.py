import collections, heapq

def findCheapestPrice(n, flights, src, dst, k):
  # create graph via adj list. Graph is directed + wieghted + possible cycles / redundent work
  adj = {i: [] for i in range(n)} # Given total flights. Would need to revist assumption in interview
  for start, finish, cost in flights: # decompossing the edges + weights given
    adj[start].append((finish, cost)) # add the edges to the verticies (directed) in our graph / adj list

  visited = collections.defaultdict(lambda: float('inf')) # track repeated work since there can be cycles -> [node] => minimum stops

  # create min heap for shortest path algo. Pop shortest relative distance
  minHeap = [(0, src, -1)] # current node, total cost, stops taken so far
  # cost starts at 0 given it takes nothing to get there, -1 stops as we need cushion of 1 for the conditional to work in the algo

  while minHeap: # keep going till we have exhausted our paths
    cost, node, stops = heapq.heappop(minHeap)
    if node == dst: # reached the end, BFS guarentees min cost from first finisher
      return cost
    if stops >= k: # Ran out of stops = non-valid solution
      continue

    visited[node] = stops # We have a min stops for that node, update but not everytime we look at neihbors

    for nei, extraCost in adj[node]: # decompose edges
      if stops + 1 < visited[nei]: # visited node already, so see if even looking at it makes sense
        heapq.heappush(minHeap, (cost + extraCost, nei, stops + 1)) # Remember, heaps sort by first value

  return -1

print(findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))