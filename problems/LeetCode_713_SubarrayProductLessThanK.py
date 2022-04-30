def numSubarray(nums, k):
    if k <= 1: return 0
    l = r = 0
    res = 0
    product = 1

    for r in range(len(nums)):
        # account for new value
        product *= nums[r]
        # check if product is more than k

        if product >= k:
            while product >= k and l <= r:
                product /= nums[l]
                l += 1
        res += r - l + 1
    return res

print(numSubarray([101,5,2,6], 100))