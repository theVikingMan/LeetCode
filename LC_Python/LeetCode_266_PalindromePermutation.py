def canPermutePalindrome(s):
  seen = {}
  for l in s:
    seen[l] = 1 + seen.get(l, 0)
    if seen[l] == 2:
      del seen[l]
  return len(seen) < 2

print(canPermutePalindrome("code")) # false
print(canPermutePalindrome("carerac")) # true