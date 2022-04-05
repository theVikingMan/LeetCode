from functools import cmp_to_key


def largestNumber(nums):
    # Stringify them so we can sort based on the combination of order
    # Ints would cause a different type of sorting
    for i in range(len(nums)):
        nums[i] = str(nums[i])

    # Create custom sort function that puts the two ints together
    # and evualtes the number when appended to eachother
    def compare(n1, n2):
        if n1 + n2 > n2 + n1:
            # -1 means don't change
            return -1
        else:
            # if n2 + n1 is larger, then 1 which evaluats to True
            return 1

    # sorted(iterable, key, reverse=False)
    res = sorted(nums, key=cmp_to_key(compare))

    # Do this to combine, lop off any leading zeros then return desired output type
    return str(int(''.join(res)))


print(largestNumber([3,30,34,5,9]))
# "9534330"