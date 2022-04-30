def findMin(nums):
    # set initial value
    res = nums[0]
    # set pointers to either side to then shift
    l, r = 0, len(nums) - 1

    while l <= r:
        if nums[l] < nums[r]:
            res = min (res, nums[l])
            break

        # Binary search portion
        m = (l + r) // 2
        res = min(res, nums[m])
        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1
    return res

print(findMin([3,4,5,6,1,2]))