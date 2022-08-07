import collections

def reverseWords(s):
  l, r = 0, len(s) - 1
  while l <= r and s[l] == " ":
    l += 1
  while l <= r and s[r] == " ":
    r -= 1

  q, word = collections.deque(), []
  while l <= r:
    if s[l] == " " and word:
      q.appendleft("".join(word))
      word = []
    elif s[l] != " ":
      word.append(s[l])
    l += 1
  q.appendleft("".join(word))
  return " ".join(q)


def reverseWords(s):
  return " ".join(reversed(s.split()))

def reverseWords(s):
  res = []
  sub = ""
  i = len(s) - 1
  while i >= 0:
    if s[i] != " ":
      sub += s[i]
    else:
      if sub:
        res.append(sub[::-1])
        sub = ""
    i -= 1
  if sub:
    res.append(sub[::-1])
  return " ".join(res)