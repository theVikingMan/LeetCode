def minSubArrLen(target, nums):
  l, total = 0, 0
  # Set to big value as we are trying to minimize
  res = float('inf')

  # Method of shifting our right pointer
  for r in range(len(nums)):
    total += nums[r]
    while total >= target:
      res = min(res, r - l + 1)
      total -= nums[l]
      l += 1

  return 0 if res == float('inf') else res