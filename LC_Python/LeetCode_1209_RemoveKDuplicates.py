def removeDuplicates(s, k):
  stack = []

  for l in s:
    if not stack or l != stack[-1][0]:
      stack.append([l, 1])
    else:
      stack[-1][1] += 1

    if stack[-1][1] == k:
      stack.pop()

  res = ""
  for l, cnt in stack:
    res += (l * cnt)
  return res

print(removeDuplicates("abbbaccca", 3))