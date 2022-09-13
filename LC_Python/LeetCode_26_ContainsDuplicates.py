def removeDuplicates(nums):
  curr, nxt, n = 0, 1, len(nums)
  if n < 2: return n

  while nxt < n:
    if nums[nxt] != nums[curr]:
      curr += 1
      nums[curr], nums[nxt] = nums[nxt], nums[curr]
    nxt += 1

  return curr + 1

print(removeDuplicates([1, 1, 2]))

# T: O(n) -> Just need to for loop once as the nxt pointer will be +1 every time
# S: O(1) -> Only pointers, no auxiliery data structures used