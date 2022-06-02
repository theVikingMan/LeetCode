import collections, heapq

def findCheapestPrice(n, flights, src, dst, k):
  adj = collections.defaultdict(list)
  for f, t, w in flights:
    adj[f].append([t, w])

  minHeap = [(0, -1, src)]
  heapq.heapify(minHeap)
  visit = collections.defaultdict(lambda: float('inf'))

  while minHeap:
    total, stopsLeft, node = heapq.heappop(minHeap)
    if stopsLeft > k:
      continue
    if visit[node] <= stopsLeft:
      continue
    if node == dst:
      return total

    visit[node] = stopsLeft

    for nei, cost in adj[node]:
      if stopsLeft + 1 <= k:
        heapq.heappush(minHeap, (total + cost, stopsLeft + 1, nei))

  return -1

print(findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))