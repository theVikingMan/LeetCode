def minMovesToMakePalindrome(s):
  s = list(s) # break string into an array
  res = 0

  while s:
      i = s.index(s[-1]) # find the left (if appl.) corresponding letter idx
      if i == len(s) - 1: # is it a single letter occurance
          res += i / 2 # move to the middle, add number of the step count to reach middle
      else:
          res += i # number of steps to move to the left boundry
          s.pop(i) # pop the left letter occurance that we just "moved"
      s.pop() # pop the corresponding letter we were analyzing
  return res

print(minMovesToMakePalindrome("aabcb"))