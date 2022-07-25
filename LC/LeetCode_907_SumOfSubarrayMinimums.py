def maxSumMinProduct(arr):
  stack = []
  res = 0

  for i, n in enumerate(arr):
    startIdx = i
    while stack and stack[-1][3] > n:
      idx, leftDiff, initialIdx, val = stack.pop()
      combos = (leftDiff + 1) * (i - initialIdx) * val
      res += combos
      startIdx = idx
    stack.append([startIdx, i - startIdx, i, n])

  for i, leftDiff, initialIdx, n in stack:
    combos = (leftDiff + 1) * (len(arr) - initialIdx) * n
    res += combos

  return res % (10**9 + 7)

print(maxSumMinProduct([3,1,2,4]))