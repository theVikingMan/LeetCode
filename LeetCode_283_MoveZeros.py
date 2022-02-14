def moveZeroes(nums):
    copy_nums = nums[::]
    zero_pointer = -1
    whole_pointer = 0
    read_pointer = 0
    while read_pointer < len(copy_nums):
        if copy_nums[read_pointer] != 0:
            nums[whole_pointer] = copy_nums[read_pointer]
            whole_pointer += 1
            read_pointer += 1
        else:
            nums[zero_pointer] = copy_nums[read_pointer]
            zero_pointer -= 1
            read_pointer += 1
    return nums


print(moveZeroes([0, 1, 0, 3, 12]))
# [1,3,12,0,0]

print(moveZeroes([0]))
# [0]
