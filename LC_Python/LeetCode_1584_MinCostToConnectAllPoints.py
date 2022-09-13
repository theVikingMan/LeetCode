import heapq

def minCostConnectPoints(points):
    # create adj list
    N = len(points)
    adj = { i: [] for i in range(N) } # i : list of [cost, node]
    for i in range(N): # loop over each point in points
        x1, y1 = points[i] # extract curr point coordinates
        for j in range(i + 1, N): # compare curr point to all other points besides itself
            x2, y2 = points[j] # extract other points coordinates to compare
            dist = abs(x1 - x2) + abs(y1 - y2) # calculate distance for each point
            adj[i].append([dist, j]) # at key i, add the other points cost
            adj[j].append([dist, i]) # at key j, add the curr point's cost

    # Prims Algorithm implementation
    res = 0
    visit = set()
    minHeap = [[0, 0]] # [cost, point]. Start at point zero
    while len(visit) < N: # Only N - 1 edges. If more, than there is a cycle
        cost, i = heapq.heappop(minHeap) # extract minimum cost point
        if i in visit: # if already looked at, dont process again
            continue
        res += cost # add fresh new node
        visit.add(i)
        for neiCost, nei in adj[i]:
            if nei not in visit: # If we do not already have an answer for the node
                heapq.heappush(minHeap, [neiCost, nei])
    return res

print(minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))


def maxSumMinProduct(points):
  res = 0
  minHeap = [[0, 0, points[0][0], points[0][1]]]
  visited = set()
  visited.add(0)

  while minHeap and len(visited) < len(points):
    dis, point, x1, y1 = heapq.heappop(minHeap)
    res += dis
    visited.add(point)
    for i in range(len(points)):
      if i not in visited and i != point:
        x2, y2 = points[i]
        distance = abs(x1-x2) + abs(y1-y2)
        heapq.heappush(minHeap, [distance, i, x2, y2])

  return res