def solution(words):
  words.sort() # sort as they will be increasing if same prefixes but more letters means higher sort order
  st, res = set(), '' # initialize a seen set to ref when building answer
  st.add(res) # begin seen set with nothing as its any word's prefix

  for w in words: # loop over the sorted words to begin building possible answer
    if w[:-1] in st: # if the current word's prefix is in our seen set
      if len(w) > len(res): # check if new max length answer
        res = w # new max, change result word
      st.add(w) # make sure to add the new possible prefix to seen set
  return res