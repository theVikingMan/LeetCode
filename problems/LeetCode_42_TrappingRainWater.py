# ask if these container questions can be negative

def trap(height):
    if not height: return 0 # check edge case of no input

    l, r = 0, len(height) - 1 # set 2 pointers up
    leftMax, rightMax = height[l], height[r] # initially start pointers at each end
    res = 0 # result variable

    while l < r: # while the pointers havent crossed or met
        if leftMax < rightMax: # if left is lower than right
            l += 1 # bring left in
            leftMax = max(leftMax, height[l]) # keep track of highest left
            res += leftMax - height[l] # heighest left minus current elevation
        else: # right elevation is lower
            r -= 1 # bring in right elevation
            rightMax = max(rightMax, height[r]) # get new max
            res += rightMax - height[r] # heighest right minus current elevation
    return res

    # This strategy accounts for the sides of the container and new heights
    # which is why we add to the res once moved and the moving of the lower pointers will always
    # yield a viable answer
print(trap([4,2,0,3,2,5]))