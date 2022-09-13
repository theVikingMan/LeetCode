import math

def constructRectangle(area):
  m = int(math.sqrt(area))
  while m > 0:
    if area % m == 0:
      return [(area / m), m]
    m -= 1


print(constructRectangle(21))