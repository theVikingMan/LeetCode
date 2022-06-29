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