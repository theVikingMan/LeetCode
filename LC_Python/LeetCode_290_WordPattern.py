def wordPattern(pattern, s):
  sBroken = s.split(" ")
  if len(pattern) != len(sBroken):
    return False
  mapping = {}
  words = {}

  for i, letter in enumerate(pattern):
    word = sBroken[i]
    if letter not in mapping and word not in words:
      mapping[letter] = word
      words[word] = letter
    elif letter in mapping and mapping[letter] != word:
      return False
    elif word in words and words[word] != letter:
      return False

  return True