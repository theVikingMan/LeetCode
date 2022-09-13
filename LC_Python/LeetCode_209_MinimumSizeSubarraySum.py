def minSubArrLen(target, nums):
  l, total = 0, 0
  res = float('inf') # Set to big value as we are trying to minimize

  for r in range(len(nums)): # Method of shifting our right pointer
    total += nums[r]
    while total >= target: # while loop is the sliding window for the L pointer
      res = min(res, r - l + 1) # constantly update res for the length given valid input
      total -= nums[l] # clean up nums
      l += 1

  return 0 if res == float('inf') else res