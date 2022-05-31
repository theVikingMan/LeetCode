import collections
import heapq

def solution(tasks, n):
  count = collections.Counter(tasks) # Get the count of all the chars
  maxHeap = [-cnt for cnt in count.values()] # Create max heap
  heapq.heapify(maxHeap)

  time = 0
  q = collections.deque() # Double ended queue that has pairs of [-cnt, idleTime]
                          # IdleTime tells us when we can add back to the heap
  while maxHeap or q:
    time += 1
    if maxHeap: # If we have items to process intitially or whose time has come up
      cnt = 1 + heapq.heappop(maxHeap) # We are processing the task
      if cnt:
        q.append([cnt, time + n]) # If there is still instances for that count, have it be in waiting
    if q and q[0][1] ==  time:
      heapq.heappush(maxHeap, q.popleft()[0])
  return time

print(solution(["A","A","A","B","B","B"], 2))