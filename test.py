def numSubarrayProductLessThanK(nums, k):
  l, r, n = 0, 0, len(nums)

  result, curr = 0, 1
  while r < n:
    curr *= nums[r]
    while curr >= k:
      curr /= nums[l]
      l += 1
    result += r - l + 1
    r += 1
  return result

print(numSubarrayProductLessThanK([10,5,2,6], 100))