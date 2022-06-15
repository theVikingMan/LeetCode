def solution(nums):
  res = 0
  l, r = 0, 0

  while r < len(nums) - 1:
    farthest = 0
    for i in range(l, r + 1):
      farthest = max(farthest, nums[i] + i)
    l = r + 1
    r = farthest
    res += 1
  return res

# T: O(n)
# S: O(1)
# Algo: Greedy

print(solution([2,3,1,1,4])) # Output: 2
# print(solution([2,3,0,1,4])) # Output: 2

# -------------- DP / Slower Solution --------------#
# T: O(n^2)

# def solution(nums):
#   numsLen = len(nums)
#   if numsLen == 1:
#     return 0

#   res = [float('inf') for _ in range(numsLen)]
#   res[-1] = 0
#   resMin = float('inf')

#   for i in range(numsLen - 2, -1, -1):
#     minEnd = min(i + nums[i], numsLen - 1)
#     for j in range(i, minEnd + 1):
#       res[i] = min(1 + res[j], res[i])
#     resMin = min(res[i], resMin)
#   return res[0]