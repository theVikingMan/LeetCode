import heapq

def solution(array):
  res = []
  minH = []
  for i, arr in enumerate(array):
    heapq.heappush(minH, [arr[0], i, 0])
  while minH:
    val, arrIdx, idx = heapq.heappop(minH)
    res.append(val)
    if idx + 1 < len(array[arrIdx]):
      heapq.heappush(minH, [array[arrIdx][idx+1], arrIdx, idx+1])
  return res



print(solution([[1,3,5,5,9], [0], [10,11], [2,3,4,5], [6,6,7]]))