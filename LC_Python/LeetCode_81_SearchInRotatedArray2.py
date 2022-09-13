def search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        while l < r and nums[l] == nums[l+1]:
            l += 1
        while l < r and nums[r] == nums[r-1]:
            r -= 1
        m = (l + r) // 2
        if target == nums[m]:
            return True

        # check if we are in the left sorted portion  (the larger half)
        if nums[l] <= nums[m]:
            # check to see if the target is in our sorted portion and if not,
            # its in the right sorted portion and need to basically move the search
            # to the whole other half
            if target > nums[m] or target < nums[l]:
                l = m + 1
            else:
                r = m - 1
        # right sorted portion (the smaller half)
        else:
            if target < nums[m] or target > nums[r]:
                r = m - 1
            else:
                l = m + 1
    return False