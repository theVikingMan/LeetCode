def fullJustify(words, maxWidth):
  res = []
  i = 0 # pointer to whatever word we are at
  width = 0 # store current width of current line
  cur_line = [] # current line for all of our words

  while i < len(words):
    curWord = words[i]
    if width + len(curWord) <= maxWidth:
      cur_line.append(curWord)
      width += len(curWord) + 1 # +1 space for each word
      i += 1
    else: # not allowed to take the current word
      spaces = maxWidth - width + len(cur_line) # normalize for all spaces out of width
      added = 0
      j = 0
      while added < spaces:
        if j >= len(cur_line) - 1: # preventing the last word in the line from a space
          j = 0

        cur_line[j] += " "
        added += 1
        j += 1
      res.append("".join(cur_line))
      cur_line = []
      width = 0

  for w in range(len(cur_line) - 1): # add the single spaces to the last rows words but not the end
    cur_line[w] += " "
  cur_line[-1] += " " * (maxWidth - width + 1)
  res.append("".join(cur_line))
  return res

print(fullJustify(["This", "is", "an", "example", "of", "text", "bo", "justification."], 16))