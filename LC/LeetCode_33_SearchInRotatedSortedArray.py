def search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r: # while our pointers havent crossed meaning no solution
        m = (l + r) // 2 # calculate the middle
        if target == nums[m]: # constantly checking if we found the answer
            return m

        # check if we are in the left sorted portion
        if nums[l] <= nums[m]:
            # if its not in that portion, move to the potentional right portion
            # or the rest of the left sorted portion
            if target > nums[m] or target < nums[l]:
                l = m + 1
            # if possible in the current left porition, move in on current portion
            else:
                r = m - 1
        # middle pointer is in the right sorted portion
        else:
            # Check if there are lower numbers in the right portiion (portion with lower nums)
            # checking if we it ourside our current porition so we would need to move to the larger set
            if target < nums[m] or target > nums[r]:
                r = m - 1
            else:
                l = m + 1
    return -1

print(search([4,5,6,7,0,1,2], 0))