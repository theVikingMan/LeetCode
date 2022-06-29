import collections
import heapq

def maxProbability(n, edges, succProb, start, end):
  # STEP 1: set up adjcency list for undirected graph (2 way)
  adj = collections.defaultdict(list)
  for (par, child), prob in zip(edges, succProb):
    adj[par].append((child, prob))
    adj[child].append((par, prob))

  visit = collections.defaultdict(int)
  p = -1 # need to start it negative for future transformations
  maxHeap = [(-1, start)] # initial starting point. Cost is 0 to begin

  # STEP 2: Use heap to find nearest point
  while maxHeap:
    p1, n1 = heapq.heappop(maxHeap) # nearest point on current heap
    if n1 in visit: # seen it before
      continue # Do not analyze again
    p = max(p, p1) # we want highest probabilty which converges on zero
    visit[n1] = p # mark as visited
    for n2, p2 in adj[n1]: # go through adj neis and add to heapw
      if n2 not in visit:
        heapq.heappush(maxHeap, (-1 * abs(p1 * p2), n2)) # -1 to keep it a MAX HEAP
  return abs(visit[end]) if end in visit else 0

print(maxProbability(5, [[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]], [0.37,0.17,0.93,0.23,0.39,0.04], 3, 4))