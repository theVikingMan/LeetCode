def moveZeroes(nums):
  l = 0

  for r in range(len(nums)):
    if nums[r]:
      nums[l], nums[r] = nums[r], nums[l]
      l += 1
  return nums


print(moveZeroes([0, 1, 0, 3, 12]))
# [1,3,12,0,0]

print(moveZeroes([0]))
# [0]
