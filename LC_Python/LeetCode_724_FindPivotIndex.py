def pivotIndex(nums):
  total = sum(nums)
  left = 0

  for i in range(len(nums)):
    right = total - nums[i] - left
    if right == left:
      return i
    left += nums[i]
  return -1

# T: O(n)
# S: O(1) -> only use single variables