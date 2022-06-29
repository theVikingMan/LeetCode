import collections
import heapq

def networkDelayTime(times, n, k):
  edges = collections.defaultdict(list)
  for u, v, w in times: # creating adj list with target node and its neighbors, time to neighbor
    edges[u].append((v, w)) # DAG -> one direction of adj lists

  minHeap = [(0, k)] # (total path cost, node)
  visit = set() # cycle detection (as per usual)
  t = 0 # max cost to visit last node
  while minHeap: # while there are still nodes to explore
    w1, n1 = heapq.heappop(minHeap)
    if n1 in visit: # if we have already seen it, we don't want to go through its neighbors again
      continue
    visit.add(n1)
    t = max(t, w1) # BFS style so the max weight will be how long it takes to visit unless
                   # a new path pushes that upper bound
    for n2, w2 in edges[n1]: # for all neighbors, visit only if not seen
      if n2 not in visit:
        heapq.heappush(minHeap, (w1 + w2, n2))

  return t if len(visit) == n else -1

print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))

# T: O(E * log(v))