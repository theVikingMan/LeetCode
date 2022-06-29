def solution(s1, s2):
    if len(s1) > len(s2): return False

    s1Count, s2Count = [0] * 26, [0] * 26
    for i in range(len(s1)): # Get the ASCH count for each string up to the length of s1
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1

    matches = 0
    for i in range(26):
        matches += (1 if s1Count[i] == s2Count[i] else 0) # if any overlapping chars, even 0s
        # this DOES NOT take care of ordering, just count of chars
    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26: return True

        index = ord(s2[r]) - ord('a')
        s2Count[index] += 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1

        index = ord(s2[l]) - ord('a')
        s2Count[index] -= 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1
        l += 1
    return matches == 26

print(solution("ab","eidbaooo"))


# -------------- Sub optimal (26 * n) -------------- #
# def solution(s1, s2):
# if len(s1) > len(s2):
#   return False

# count1 = {}
# count2 = {}

# for c in s1:
#   count1[c] = 1 + count1.get(c, 0)

# l = 0
# for r in range(len(s2)):
#   if count1 == count2:
#     return True
#   count2[s2[r]] = 1 + count2.get(s2[r], 0)
#   while l < r and (r - l + 1) > len(s1):
#     count2[s2[l]] -= 1
#     if count2[s2[l]] == 0:
#       del count2[s2[l]]
#     l += 1

# return False if count1 != count2 else True