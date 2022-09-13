def rob(nums):
    rob1, rob2 = 0, 0

    for n in nums:
        temp = max(rob1 + n, rob2) # either rob (curr + curr - 2) or just (curr - 1)
        rob1 = rob2
        rob2 = temp
    return max(rob1, rob2)

print(rob([1, 2, 3, 1]))

# ------------- Recursive w/ caching ------------- #

# def rob(arr):
#   cache = {}

#   def recurse(one, two, idx):
#     if idx == len(arr):
#       return two
#     if idx in cache:
#       return cache[idx]

#     temp = two
#     two = max(two, one + arr[idx])
#     one = temp

#     cache[idx] = recurse(one, two, idx + 1)
#     return cache[idx]

#   return recurse(0, 0, 0)