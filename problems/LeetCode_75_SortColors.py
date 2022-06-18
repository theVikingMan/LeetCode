def sortColors(nums):
    l, curr, r = 0, 0, len(nums) - 1
    while curr <= r:
        if nums[curr] == 0:
            nums[l], nums[curr] = nums[curr], nums[l]
            l += 1
            curr += 1
        elif nums[curr] == 2:
            nums[r], nums[curr] = nums[curr], nums[r]
            r -= 1
            # We might have introduced a 1/2 into the smaller part of the arr
            # So we do not move the curr this time
        else: # We found a 1, no alterations to make
            curr += 1

print([2,0,2,1,1,0])