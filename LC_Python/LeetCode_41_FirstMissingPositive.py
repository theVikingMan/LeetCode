
def firstMissingPositive(nums) -> int:
  # Handle negative numbers
  for i, element in enumerate(nums):
    if element < 0:
      nums[i] = 0

  # mark all the positive numbers seen by flipping index values
  for i in range(len(nums)):
    val = abs(nums[i])
    if 1 <= val <= len(nums): # if the current val is in-bounds
      if nums[val - 1] > 0: # find the idx val and flip
        nums[val - 1] *= -1
      elif nums[val -1] == 0: # set the val to a num that wont affect ans
        nums[val - 1] = -1 * (len(nums) + 1)

  for i in range(1, len(nums) + 1): # find the first missing num if pos
    if nums[i - 1] >= 0:
      return i

  return len(nums) + 1

print(firstMissingPositive([1,2,-1,3]))

# T: O(n) -> 3 loops always through
# S: O(1) -> Using the input array as the tracker of what nums are present