import collections
import heapq

def solution(tasks, n):
  # Get the count of all the chars
  count = collections.Counter(tasks)
  maxHeap = [-cnt for cnt in count.values()]
  heapq.heapify(maxHeap)

  time = 0
  q = collections.deque() # pairs of [-cnt, idleTime]

  while maxHeap or q:
    time += 1
    if maxHeap:
      cnt = 1 + heapq.heappop(maxHeap)
      if cnt:
        q.append([cnt, time + n])
    if q and q[0][1] ==  time:
      heapq.heappush(maxHeap, q.popleft()[0])
  return time