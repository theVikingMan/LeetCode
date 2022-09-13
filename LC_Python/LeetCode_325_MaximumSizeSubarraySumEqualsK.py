def solution(nums, k):
  res = 0
  curSum = 0
  prefix = { 0 : -1 }

  for i, n in enumerate(nums):
    curSum += n # Continually add up the prefix sum
    diff = curSum - k # Calc what num we need to have seen before to CHOP OFF
    res = max(res, i - prefix.get(diff, i))
    prefix[curSum] = prefix.get(curSum, i) # store idx rather times seen vs another problem
                                               # so you can see the pattern emerage
  return res

print(solution([-2,-1,2,1], 1))