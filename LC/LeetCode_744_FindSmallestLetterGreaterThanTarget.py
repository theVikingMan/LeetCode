def nextGreatestLetter(letters, target):
    for c in letters:
        if c > target:
            return c
    return letters[0]
