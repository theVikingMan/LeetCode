def totalFruits(fruits):
  seen = {}
  start = max_fruits = 0

  for end in range(len(fruits)):
    seen[fruits[end]] = end # Furit Number, Idx
    if len(seen) > 2:
      min_idx = min(seen.values())
      start = min_idx + 1
      del seen[fruits[min_idx]]
    max_fruits = max(max_fruits, end - start + 1)
  return max_fruits

print(totalFruits([1,2,3,2,2]))