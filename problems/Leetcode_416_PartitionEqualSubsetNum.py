def canPartition(nums):
    sumNums = sum(nums) # Reduce repeated work
    if sumNums % 2: # Answer must be even to be divided by 2
        return False

    dp = set()
    target = sumNums // 2
    dp.add(0) # initial value that allows for single number answer

    for n in nums: # Interate through all possible given values
        nextDP = set() # will keep all old products AND new products of the current given value
        for t in dp: # Interate through all of the products till now
            if (t + n) == target: # check if we found it, optimization
                return True
            nextDP.add(t + n) # add the new product to the to-be-new-all products set
            nextDP.add(t) # add the old product
        dp = nextDP
    return True if target in dp else False

print(canPartition([1,5,11,5]))