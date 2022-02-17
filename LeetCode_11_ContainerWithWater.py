def maxArea(height):
  maxCombo = 0
  l, r = 0, len(height) - 1

  while l < r:
    currArea = min(height[l], height[r]) * (r - l)
    maxCombo = max(maxCombo, currArea)
    if height[l] < height[r]:
      l += 1
    else:
      r -= 1
  return maxCombo

print(maxArea([2,3,10,5,7,8,9]))