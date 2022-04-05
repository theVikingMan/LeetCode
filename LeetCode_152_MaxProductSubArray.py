def maxProduct(nums):
    # base value of 1 which won't affect the products going forward
    curMin, curMax = 1, 1
    # base max of the whole array
    result = max(nums)

    # traverse each num in the array once
    for n in nums:
        # hold temp as we will be modifying the CURR max
        tmp = curMax * n
        # could be that its 2 negative nums
        curMax = max(n, curMax * n, n * curMin)
        # track min as it could be a huge scaler with another negative
        curMin = min(n, tmp, curMin * n)
        result = max(curMax, result)
    return result
