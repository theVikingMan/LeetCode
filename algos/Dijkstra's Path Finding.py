import collections
import heapq

def networkDelayTime(times, n, k):
  edges = collections.defaultdict(list)
  for u, v, w in times: # creating adj list with target node and its neighbors, time to neighbor
    edges[u].append((v, w))

  minHeap = [(0, k)] # (total path cost, node)
  visit = set() # cycle detection (as per usual)
  t = 0 # max cost to visit last node
  while minHeap: # while there are still nodes to explore
    w1, n1 = heapq.heappop(minHeap)
    if n1 in visit: # if we have already seen it, we don't want to go through its neighbors again
      continue
    visit.add(n1)
    t = max(t, w1)
    for n2, w2 in edges[n1]:
      if n2 not in visit:
        heapq.heappush(minHeap, (w1 + w2, n2))

  return t if len(visit) == n else -1

print(networkDelayTime([[1,2,1],[2,3,2],[1,3,2]], 3, 1))