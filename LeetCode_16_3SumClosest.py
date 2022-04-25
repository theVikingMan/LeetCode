def threeSumClosest(nums, target):
    nums.sort()
    # variable for the distance from target
    distance = float('-inf')

    # for-loop will grab the first number of the 3
    # We go up to the last two so there is space for the 2nd and 3rd nums
    for idx in range(len(nums) -2):
        # looking for the next 2 values
        l, r = idx + 1, len(nums) - 1
        # Makes a new target for the 2 sum II calc
        new_target = target - nums[idx]
        while l < r:
            # new sum of the remaining nums and checking how to move the
            # pointers
            sum_val = nums[l] + nums[r]

            # We dont care about distance -> abs()
            if abs(distance) > abs(new_target - sum_val):
                distance = new_target - sum_val

            if sum_val == new_target:
                return target
            elif sum_val < new_target:
                l += 1
            else:
                r -= 1
    return target - distance

print(threeSumClosest([-1,2,1,-4]))