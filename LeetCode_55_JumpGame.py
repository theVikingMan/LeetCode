def canJump(nums):
    # I - array of nums. num represents MAX steps can take
    # O - boolean. If can reach len(nums) - 1
    # C
    # E - 0 resets. length of 1 array

    if len(nums) == 1:
        return True

    goal = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if (i + nums[i] >= len(nums)) or (i + nums[i] >= goal):
            goal = i
    return True if goal == 0 else False