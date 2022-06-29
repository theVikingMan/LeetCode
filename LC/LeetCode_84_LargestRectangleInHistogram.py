def solution(heights):
  stack = [] # pairs (index, height)
  maxH = 0

  for i, h in enumerate(heights):
    start = i
    while stack and h < stack[-1][1]:
      oldIdx, oldH = stack.pop()
      maxH = max(maxH, (i - oldIdx) * oldH)
      start = oldIdx
    stack.append((start, h))

  for i, h in stack:
    maxH = max(maxH, (len(heights) - i) * h)
  return maxH

# print(solution([2,1,5,6,2,3]))
print(solution([3, 2]))