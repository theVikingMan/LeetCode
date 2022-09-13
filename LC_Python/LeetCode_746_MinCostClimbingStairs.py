def solution(cost):
  if not cost:
    return 0
  one, two = cost[0], cost[1]

  for i in range(2, len(cost)):
    temp = two
    two = cost[i] + min(one, two)
    one = temp
  return min(one, two)

print(solution([1,100,1,1,1,100,1,1,100,1]))