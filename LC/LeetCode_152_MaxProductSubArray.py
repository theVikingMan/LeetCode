def maxProduct(nums):
    curMin, curMax = 1, 1 # base value of 1 which won't affect the products going forward
    result = max(nums) # base max of the whole array

    # traverse each num in the array once
    for n in nums:
        tmp = curMax * n # hold temp as we will be modifying the curMax
        curMax = max(n, curMax * n, curMin * n) # could be that its 2 negative nums
        curMin = min(n, tmp, curMin * n) # track min as it could be a huge scaler with another negative
        result = max(curMax, result)
    return result
