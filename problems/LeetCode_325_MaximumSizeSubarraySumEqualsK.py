def solution(nums, k):
  res = 0
  curSum = 0
  curLen = 0
  prefixs = { 0 : 1 }

  for n in nums:
    curSum += n
    curLen += 1
    diff = curSum - k
    res = max(res, prefixs.get(diff, 0))
    prefixs[curSum] = max(curLen, prefixs.get(curSum, 0))
  return res

print(solution([-2,-1,2,1], 1))