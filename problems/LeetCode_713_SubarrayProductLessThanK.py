def numSubarray(nums, k):
    if k <= 1: return 0
    res, temp, l = 0, 1, 0

    for i in range(len(nums)):
      temp *= nums[i] # multiply by new number
      while temp >= k and l <= i: # while our res is invalid and l hasn't crossed over
        temp /= nums[l]
        l += 1
      res += (i - l + 1) # captures all the additional individual nums and the additional combination
    return res

print(numSubarray([101,5,2,6], 100))