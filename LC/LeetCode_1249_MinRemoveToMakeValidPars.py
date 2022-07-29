def minRemoveToMakeValid(s):
  left, right = 0, 0
  res = []

  # Phase 1: handle closing paras -> closing < open
  for letter in s:
    if letter == "(":
      left += 1
      res.append(letter)
    elif letter == ")":
      if left > right:
        right += 1
        res.append(letter)
    else:
      res.append(letter)

  if left == right:
    return "".join(res)

  otherRes = []
  # Phase 2: handle opening paras -> open <= close
  for i in range(len(res) - 1, -1, -1):
    letter = res[i]
    if letter == "(":
      if left <= right:
        otherRes.append(letter)
      else:
        left -= 1
    else:
      otherRes.append(letter)

  return "".join(otherRes[::-1])