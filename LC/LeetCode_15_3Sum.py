def threeSum(nums):
  res = []
  nums.sort() # must sort to use the 2-pointer strategy

  for idx, a in enumerate(nums): # for-loop of our first num (a in this case)
    if idx > 0 and a == nums[idx - 1]: # check if duplicate when not first char
      continue

    l, r = idx + 1, len(nums) - 1 # 2 other pointers for the 2nd & 3rd digits
    while l < r: # pointers cannot be the same num
      threeSum = a + nums[l] + nums[r] # current 3 sum
      if threeSum > 0: # we are over Zero aka target -> move in the right pointer located at the larger numbers
        r -= 1
      elif threeSum < 0: # move left if under 0, increasing curr 3 sum
        l += 1
      else:
        res.append([a, nums[l], nums[r]]) # we have found one answer of possible many
        l += 1 # shift our left pointer to start a new journey

        while nums[l] == nums[l - 1] and l < r: # classic while loop to avoid duplicates with l pointer
          l += 1
  return res

print(threeSum([-1,0,1,2,-1,-4]))

# T: O(n^2) -> potentially have to look over all the elements (2sum) and sort(n * log(n))
# S: O(1) -> only pointers but result variable or sorting could add space (log n for sorting)

# STRATEGY
# 3 pointers. Using for loop for 1st, then 2 pointers for the last 2
# Array must be sorted for this to work with 2 pointers