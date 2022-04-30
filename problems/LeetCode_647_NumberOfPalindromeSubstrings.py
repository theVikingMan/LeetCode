def countSubstrings(self, s):
    # I - string of letters
    # O - number of substrings that a palindromes. single letters are valid
    # C
    # E - 1 length string

    count = 0

    for i in range(len(s)):
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1

        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
    return count