def threeSumClosest(nums, target):
    nums.sort()
    distance = float('-inf') # variable for the distance from target

    # for-loop will grab the first number of the 3
    # We go up to the last two so there is space for the 2nd and 3rd nums
    for idx in range(len(nums) -2):
        l, r = idx + 1, len(nums) - 1 # looking for the next 2 values == 2Sum
        new_target = target - nums[idx] # Makes a new target for the 2 sum II calc
        while l < r:
            sum_val = nums[l] + nums[r] # sum of last 2 curr pointers
            if abs(distance) > abs(new_target - sum_val):  # We dont care about distance -> abs()
                distance = new_target - sum_val
            if sum_val == new_target: # Found perfect match
                return target
            elif sum_val < new_target:
                l += 1
            else:
                r -= 1
    return target - distance

print(threeSumClosest([-1,2,1,-4]))