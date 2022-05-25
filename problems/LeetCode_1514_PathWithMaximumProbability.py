import collections
import heapq

def maxProbability(n, edges, succProb, start, end):
  adj = collections.defaultdict(list)
  for (par, child), prob in zip(edges, succProb):
    adj[par].append((child, prob))
    adj[child].append((par, prob))

  visit = collections.defaultdict(int)
  p = -1
  maxHeap = [(-1, start)]

  while maxHeap:
    p1, n1 = heapq.heappop(maxHeap)
    if n1 in visit:
      continue

    p = max(p, p1)
    visit[n1] = p
    for n2, p2 in adj[n1]:
      if n2 not in visit:
        heapq.heappush(maxHeap, (-1 * abs(p1 * p2), n2))
  return abs(visit[end]) if end in visit else 0

print(maxProbability(5, [[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]], [0.37,0.17,0.93,0.23,0.39,0.04], 3, 4))