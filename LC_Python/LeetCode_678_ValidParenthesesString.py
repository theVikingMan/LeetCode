def checkValidString(s):
  leftMin, leftMax = 0, 0

  for par in s:
    if par == '(':
      leftMin, leftMax = leftMin + 1, leftMax + 1
    elif par == ')':
      leftMin, leftMax = leftMin - 1, leftMax - 1
      if leftMax < 0:
        return False
    else:
      leftMin, leftMax = leftMin - 1, leftMax + 1
    if leftMin < 0:
      leftMin = 0
  return leftMin == 0

print(checkValidString("(*)))"))