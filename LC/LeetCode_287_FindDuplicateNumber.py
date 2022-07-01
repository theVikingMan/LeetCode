# ---------------- Floyd's Cycle Detections ---------------- #

def findDuplicate(nums):
    slow, fast = 0, 0
    while True: # Do-while loop for the pointers to hit each other
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow2 = 0
    while True: # Do-while loop till the 2 slow pointers meet which will be the location of the cycle
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow

# T: O(n)
# S: O(1)

print(findDuplicate([1,3,4,2,2]))