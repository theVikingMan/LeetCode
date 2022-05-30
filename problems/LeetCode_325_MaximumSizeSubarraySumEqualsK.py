def solution(nums, k):
  res = 0
  curSum = 0
  prefix = { 0 : 0 }

  for i, n in enumerate(nums):
    curSum += n
    diff = curSum - k
    res = max(res, i - prefix.get(diff, i + 1) + 1)
    prefix[curSum] = prefix.get(curSum, i + 1)

  return res

print(solution([-2,-1,2,1], 1))