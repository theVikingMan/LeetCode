def generateAbbreviations(word):
    result = []

    def backtracking(count, curr, idx):
        if idx == len(word):
            result.append(curr + str(count) if count > 0 else curr)
        else:
          # Decision 1: Increase count and move on to the next letter
            backtracking(count + 1, curr, idx + 1)
          # Decision 2: Add a letter which kills the count, add the count prior to the letter
          # due to our constraint and move on to the next letter for another choice
            backtracking(0, curr + (str(count) if count > 0 else '') + word[idx], idx + 1)

    backtracking(0, '', 0)
    return result

print(generateAbbreviations("word"))