def triangleNumber(nums):
  res = 0
  nums.sort()

  for i in range(len(nums) -1 , 1, -1):
    l = 0
    r = i - 1
    while l < r:
      curr = nums[l] + nums[r]
      if curr <= nums[i]:
        l += 1
      else:
        res += (r - l)
        r -= 1
  return res

print(triangleNumber([2,2,3,4]))