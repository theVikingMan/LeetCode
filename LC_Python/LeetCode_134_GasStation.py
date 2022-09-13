def solution(gas, cost):
  if sum(gas) < sum(cost):
    return -1

  res = 0
  total = 0

  for i in range(len(gas)):
    total += (gas[i] -  cost[i])
    if total < 0:
      res = i + 1
      total = 0

  return res

# T: O(n)
# S: O(1)

print(solution([1,2,3,4,5],[3,4,5,1,2])) # Output: 3


# ------------ Brute force / O(n^2) Solutino ------------ #
# def solution(gas, cost):
#   for i in range(len(gas)):
#     currTotal = gas[i] - cost[i]
#     if currTotal >= 0:
#       for j in range(1, len(gas) + 1):
#         modedIdx = (i + j) % (len(gas))
#         currTotal += gas[modedIdx] - cost[modedIdx]
#         if modedIdx == i:
#           return i
#         if (currTotal < 0):
#           break

#   return -1