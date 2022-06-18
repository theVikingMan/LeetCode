def rob(nums):
    if len(nums) < 2:
      return nums[0]

    def helper(arr):
      before, after = 0, arr[0]
      for i in range(1, len(arr)):
          temp = after
          after = max(temp, before + arr[i])
          before = temp
      return after

    # either rob the 1st house and not the last OR the last and not the firsts
    return max(helper(nums[0:len(nums)-1]), helper(nums[1:]))

print(rob([1,2,1,1]))