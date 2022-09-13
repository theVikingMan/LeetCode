def maxSumMinProduct(nums):
  prefixs = [0]
  for i, n in enumerate(nums):
    prefixs.append(prefixs[-1] + n)

  res = 0
  stack = []

  for i, n in enumerate(nums):
    startIdx = i
    while stack and stack[-1][0] > n:
      val, start = stack.pop()
      maxSum = (prefixs[i] - prefixs[start]) * val
      res = max(res, maxSum)
      startIdx = start
    stack.append([n, startIdx])

  for val, i in stack:
    maxSum = (prefixs[len(nums)] - prefixs[i]) * val
    res = max(res, maxSum)

  return res % (10**9 + 7)

print(maxSumMinProduct([1,2,3,2]))