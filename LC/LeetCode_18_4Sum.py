def fourSum(nums, target):
    nums.sort() # Must sort to eliminate duplicates and able to use 2-pointer
    res, quad = [], [] # For the recursive solution

    # k: how many values we need to make target, start: starting idx
    def kSum(k, start, target): # passing target bc it will be changing
        if k != 2: # if we have not hit the two situation aka just 2 numbers to find that are sorted
            for i in range(start, len(nums) - k + 1): # loop over the array except the remaining amount of vals
                if i > start and nums[i] == nums[i - 1]: # Avoids duplicates in the recursive calls
                    continue
                quad.append(nums[i]) # update the quad for the new potential num in nums
                kSum(k - 1, i + 1, target - nums[i]) # Simulates as many for-loops as we need with recursion
                quad.pop() # clean up call given quad is the only external variable manipulated
            return
        # ----- Two Sum II ---- #
        l, r = start, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else: # found an answer
                res.append(quad + [nums[l], nums[r]]) # python way of adding 2 lists together
                while l < r and nums[l] == nums[l + 1]: # see if there other answers and avoid duplicates
                    l += 1
                l += 1
    kSum(4, 0, target)
    return res

print(fourSum([1,0,-1,0,-2,2], 0))