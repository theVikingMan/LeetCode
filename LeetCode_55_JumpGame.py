def canJump(nums):
    if len(nums) == 1:
        return True

    goal = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if (i + nums[i] >= len(nums)) or (i + nums[i] >= goal):
            goal = i
    return True if goal == 0 else False