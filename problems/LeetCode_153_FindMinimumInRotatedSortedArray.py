def findMin(nums):
    res = nums[0] # set initial value at the first element, not max
    l, r = 0, len(nums) - 1 # set up binary search pointers

    while l <= r:
        if nums[l] < nums[r]: # if we have found a strictly increasing portion, l is min of that section
            res = min (res, nums[l])
            break

        # Set up binary search portion
        m = (l + r) // 2
        res = min(res, nums[m])

        if nums[m] >= nums[l]: # If we are in the left portion (larger nums), move towards the
                               # right portion (smaller nums)
            l = m + 1
        else:
            r = m - 1 # m pointer is in the right portion so move it to see if there is more to the
                      # right porition

    return res

print(findMin([3,4,5,6,1,2]))