import math

def solution(piles, h):
  l, r = 1, max(piles) # we can eat 1 banana or the largest amount of bananas, not more or less than those
  res = r # trying to find min so the max is our upper bounds

  while l <= r: # while our left and right pointers are in the correct order
    k = (l + r) // 2 # compute mid of the possible range of rates
    hours = 0
    for p in piles: # calculate sum of total hours for each pile with the k rate
      hours += math.ceil(p / k) # for LC ceil not working => hours += (p + k - 1) / k
    if hours <= h: # if we have a valid answer in which you can eat all bananas before the guards come back
      res = min(res, k)
      r = k - 1 # we found an answer but search if possible smaller rate answer
    else: # need to search faster rates to have a possible valid answer
      l = k + 1

  return res

print(solution([3,6,7,11], 8))