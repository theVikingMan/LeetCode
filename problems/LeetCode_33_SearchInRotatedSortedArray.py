def search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2
        if target == nums[m]:
            return m

        #check if we are in the left sorted portion
        if nums[l] <= nums[m]:
          # if its not in that portion, move to the right portion
            if target > nums[m] or target < nums[l]:
                l = m + 1
            else:
                r = m - 1
        # middle pointer is in the right sorted portion
        else:
            if target < nums[m] or target > nums[r]:
                r = m - 1
            else:
                l = m + 1
    return -1