

def findMissingRanges(nums, lower, upper):
  res = []

  i = 0
  while i <= len(nums):
    item = nums[i]+1 if i < len(nums) else lower
    nextItem = nums[i+1]-1 if (i + 1) < len(nums) else upper
    distance = nextItem - item

    if distance >= 0:
      if distance == 0:
        res.append(f"{item}")
      else:
        res.append(f"{item}->{nextItem}")
    i += 1
  return res

# def findMissingRanges(nums, lower, upper):
#   setNums = set(nums)
#   res = []
#   i = lower
#   while i <= upper:
#     minNum, maxNum = upper+1, lower-1
#     while i not in setNums and i < upper + 1:
#       minNum, maxNum = min(minNum,i) , max(maxNum, i)
#       i += 1
#     if minNum != upper+1 and maxNum != lower-1:
#       if minNum != maxNum:
#         res.append(f"{minNum}->{maxNum}")
#       else:
#         res.append(str(minNum))
#     i += 1
#   return res

print(findMissingRanges([], 1, 1))