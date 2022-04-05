def canPartition(nums):
    sumNums = sum(nums)
    # Check if even possible to have an answer as we need a to divide
    # the sum by 2 parts with no remaining value
    if sumNums % 2 == 1:
        return False

    dp = set()
    target = sumNums // 2
    # Have some initial value to add to with the initial given value
    # that doesn't mess with algo
    dp.add(0)
    # Interate through all possible given values
    for n in nums:
        # will keep all old products AND new products of the current given value
        nextDP = set()
        # Interate through all of the products till now
        for t in dp:
            # check if we found it, optimization that makes the algo faster
            if (t + n) == target:
                return True
            # add the new product to the to-be-new-all products set
            nextDP.add(t + n)
            # add the old product (which will include the base individual nums)
            nextDP.add(t)
        dp = nextDP
    return True if target in dp else False

print(canPartition([1,5,11,5]))