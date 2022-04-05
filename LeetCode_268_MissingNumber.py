def missingNumber(nums):
  missing = len(nums)
  for idx, num in enumerate(nums):
      # Index and the num should XOR to 0 and then all that is left
      # is the missing num which hasnt been XOR'd away
      missing ^= num ^ idx
  return missing

print(missingNumber([1,0,2]))

# Solution using set()
  # new_nums = set(nums)
  # for i in range(len(nums) + 1):
  #     if i not in new_nums:
  #         return i

# Another way
  # res = len(nums)
  # for i in range(len(nums)):
  #   res += (i - nums[i])
  # return res