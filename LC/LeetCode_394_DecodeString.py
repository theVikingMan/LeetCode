def decodeString(s):
  stack = []

  for i in range(len(s)):
    if s[i] != ']':
      stack.append(s[i])
    else:
      substring = ""
      while stack[-1] != "[":
        substring = stack.pop() + substring # keeps original ordering of chars
      stack.pop() # for opening bracket

      k = ""
      while stack and stack[-1].isdigit(): # need to grab whole mutli num (i.e., '57')
        k = stack.pop() + k
      stack.append(int(k) * substring)
  return "".join(stack)

print(decodeString("3[a]2[bc]"))