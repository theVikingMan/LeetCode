
# ----------- SLIDING WINDOW ------------- #

def solution(s):
  seenSet = set() # create set to hold all the seen values in our window
  res = l = 0

  for r in range(len(s)): # for loop creates our right pointer
    while s[r] in seenSet: # while there are seen repeated chars
      seenSet.remove(s[l])
      l += 1 # close the window
    seenSet.add(s[r]) # now the right pointer has a unqie char
    res = max(res, r - l + 1)
  return res

print(solution('bbbbaba'))