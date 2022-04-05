def lengthOfLIS(nums):
    # I - Array of integers (negative, 0 and positive)
    # O - Single num for length of consecutive stictly increasing nums (no fallbacks)
    #     We can delete nums too but not re-order
    # E - If no increase in the nums = 1

    # Step 1: create an array to store any given state's answer
    # Step 2: Initialize each state to one as that is the base longest answer
    LIS = [1] * len(nums)

    # Work backwards
    for i in range(len(nums) - 1, -1, -1):
        # Work forwards from starting point to check all other states
        # for potential additions to current state
        for j in range(i+1, len(nums)):
            # Step 3: Find the recurrance relationship
            if nums[i] < nums[j]:
                # Dynamic maxing as the second for loop find other states and
                # updates itself so it might find 2 + 1 then find a 1 + 1 then a 4 + 1
                # keeps track of the ONGOING nested loop max
                LIS[i] = max(LIS[i], 1 + LIS[j])
    return max(LIS)


print(lengthOfLIS([0,1,0,3,2,3]))