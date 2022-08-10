# --------------- Binary Search (accepted) --------------- #

def minimumHealth(damage, armor):
  return 1 + sum(damage) - min(max(damage), armor)

print(minimumHealth([2,7,4,3], 4))

# T: O(n) -> n being the length of the input array
# S: O(1) -> only keeping 2 integer variables

# --------------- Binary Search (accepted) --------------- #

def minimumHealth(damage, armor):
  maxDam, sumDam = max(damage), sum(damage) + 1
  l, r = 0, sumDam

  while l <= r:
    hasArmor = True
    currHealth = (l + r) // 2
    for d in damage:
      if d == maxDam and hasArmor:
        currHealth -= (max(d - armor, 0))
        hasArmor = False
      else:
        currHealth -= d

    if currHealth < 1:
      l = (l + r) // 2 + 1
    elif currHealth > 1:
      r = (l + r) // 2 - 1
    else:
      return (l + r) // 2

# T: O(n * log(n)) -> n being the length of the input array and need to search that array
# S: O(1) -> only keeping integer variables, no external DS