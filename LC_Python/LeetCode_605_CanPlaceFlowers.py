def canPlaceFlowers(flowerbed, n):
    empty = 0 if flowerbed[0] else 1 # repr the situation of [0] on the left side

    for f in flowerbed:
      if f:
        n -= int((empty - 1) / 2) # have to do this to stop any rounds down below 0
        empty = 0
        if n == 0:
          return True
      else:
        empty += 1

    n -= (empty) // 2 # repr the situation of [0] on the right side
    return n <= 0

print(canPlaceFlowers([1,0,0,0,1,0,0], 2))

# T: O(n) -> one for-loop
# S: O(1) -> using empty to repr a [0] added to each side

# def canPlaceFlowers(flowerbed, n):
#   if n == 0:
#     return True

#   flowerbed = [0] + flowerbed + [0]
#   for i in range(1, len(flowerbed) - 1):
#     if flowerbed[i] != 1 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
#       n -= 1
#       flowerbed[i] = 1
#       if n == 0:
#         return True

#   return False

# T: O(n) -> one for-loop
# S: O(n) -> [0] added to each side + basically creating a new arr (line 25)
