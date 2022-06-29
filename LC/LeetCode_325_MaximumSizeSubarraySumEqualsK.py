def solution(nums, k):
  res = 0
  curSum = 0
  prefix = { 0 : 0 }

  for i, n in enumerate(nums):
    curSum += n # Continually add up the prefix sum
    diff = curSum - k # Calc what num we need to have seen before
    res = max(res, i - prefix.get(diff, i + 1) + 1)
    prefix[curSum] = prefix.get(curSum, i + 1) # store idx rather times seen vs another problem
                                               # so you can see the pattern emerage
  return res

print(solution([-2,-1,2,1], 1))