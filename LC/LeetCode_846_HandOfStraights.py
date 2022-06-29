import heapq

def solution(hand, groupSize):
  if len(hand) % groupSize:
    return False

  count = {}
  for num in hand:
    count[num] = 1 + count.get(num, 0)

  minH = list(count.keys())
  heapq.heapify(minH)

  while minH:
    firstMin = minH[0]
    for i in range(firstMin, firstMin + groupSize):
      if i not in count:
        return False
      count[i] -= 1
      if count[i] == 0:
        if i != minH[0]:
          return False
        heapq.heappop(minH)

  return True

print(solution([8,10,12], 3))