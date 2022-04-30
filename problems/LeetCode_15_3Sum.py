def threeSum(nums):
  res = []
  nums.sort()

  # for-loop of our first num (a in this case)
  for idx, a in enumerate(nums):
    # initial check base case of if duplicate
    if idx > 0 and a == nums[idx - 1]:
      continue

    # 2 other pointers for the 2nd & 3rd digits
    l, r = idx + 1, len(nums) - 1
    while l < r:
      # whats our current sum
      threeSum = a + nums[l] + nums[r]
      # we are over Zero -> move in the right pointer located at the
      # larger numbers
      if threeSum > 0:
        r -= 1
      # move left if under
      elif threeSum < 0:
        l += 1
      else:
        # we have found an answer
        res.append([a, nums[l], nums[r]])
        # shift our left pointer to start a new journey
        l += 1
        # classic while loop to avoid duplicates
        while nums[l] == nums[l - 1] and l < r:
          l += 1
  return res

print(threeSum([-1,0,1,2,-1,-4]))