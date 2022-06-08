import collections, heapq

def findTheCity(n, edges, distanceThreshold):
    # create adj list for cyclic graph
    adj = { i:[] for i in range(n) }
    for pre, after, weight in edges:
      adj[pre].append([after, weight])
      adj[after].append([pre, weight])

    # min heap for shortest path, tracking cost

    visit = {}
    for i in range(n):
      visit[i] = set()

    def getCityCount(c):
      minHeap = [[0, c]] # total cost, start node

      while minHeap:
        curCost, node = heapq.heappop(minHeap)
        if node in visit[c]:
          continue
        if node != c:
          visit[c].add(node)

        for nei, extraCost in adj[node]:
          total = curCost + extraCost
          if nei not in visit[c] and total <= distanceThreshold:
            heapq.heappush(minHeap, [total, nei])

    for i in range(n):
      getCityCount(i)

    res = [0, float('inf')]
    for k in visit.keys():
      if len(visit[k]) <= res[1]:
        res = [k, len(visit[k])]
    return res[0]

print(findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4))
print(findTheCity(6, [[0,3,7],[2,4,1],[0,1,5],[2,3,10],[1,3,6],[1,2,1]], 417))
print(findTheCity(6, [[0,1,10],[0,2,1],[2,3,1],[1,3,1],[1,4,1],[4,5,10]], 20))