
def findMaxLength(nums):
  seen = {0: -1}
  count = res = 0
  for i, n in enumerate(nums):
    if n == 0:
      count -= 1
    else:
      count += 1

    if count in seen:
      res = max(res, i - seen[count])
    else:
      seen[count] = i
  return res

print(findMaxLength([0,0,0,1,0,1,0,0]))