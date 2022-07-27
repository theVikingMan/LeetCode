def maxOperations(nums, k):
  mapping = {}
  res = 0

  for n in nums:
    target = k - n
    if target in mapping and mapping[target] > 0:
      mapping[target] -= 1 # say we have used the num in another pair
      res += 1
    else:
      mapping[n] = 1 + mapping.get(n, 0) # increase the amount available
  return res

print(maxOperations([1,2,3,4,5], 6))

# T: O(n) -> n is the size of the array
# S: O(n) -> n is the size of the array

# ---------- Two Pointer w/ Sorting (valid, optimized space) -------- #

def maxOperations(nums, k):
  nums.sort()
  l, r = 0, len(nums) - 1
  res = 0

  while l < r:
    currSum = nums[l] + nums[r]
    if currSum < k:
      l += 1
    elif currSum > k:
      r -= 1
    else:
      l += 1
      r -= 1
      res += 1
  return res