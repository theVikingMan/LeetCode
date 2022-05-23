import collections

def countCharacters(words, chars):
    counts = collections.Counter(chars) # get the availaiblity of all chars
    res = 0

    for w in words:
        flag = True # will tell us if we have made the word which then we can add to res
        for l in w:
            if w.count(l) > counts[l]: # are there enough counts of the letter
                flag = False # Nope, means the word cant be made
                break
        if flag: # We found an answer
            res += len(w)
    return res

print(countCharacters(["cat","bt","hat","tree"], "atach"))