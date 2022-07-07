
def minFlips(s):
  n = len(s)
  s = s + s
  res = float('inf')
  alt1, alt2 = '', ''
  for i in range(len(s)):
    alt1 += "0" if i % 2 else "1"
    alt2 += "1" if i % 2 else "0"

  diff1, diff2 = 0, 0
  l = 0

  for r in range(len(s)):
    if s[r] != alt1[r]:
      diff1 += 1
    if s[r] != alt2[r]:
      diff2 += 1

    if (r - l + 1) > n:
      if s[l] != alt1[l]:
        diff1 -= 1
      if s[l] != alt2[l]:
        diff2 -= 1
      l += 1
    if (r - l + 1) == n:
      res = min(res, diff1, diff2)
  return res

print(minFlips("011"))
print(minFlips("01001001101"))
