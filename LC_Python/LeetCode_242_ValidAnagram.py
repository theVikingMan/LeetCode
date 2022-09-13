
def solution(s, t):
    dictA, dictB = [0] * 26, [0] * 26
    for letter in s:
        dictA[ord(letter) - ord('a')] += 1
    for letter in t:
        dictB[ord(letter) - ord('a')] += 1
    return dictA == dictB

print(solution('abb', 'abbb'))

# ------ OR ------

# def solution(s, t):
#   return (sorted(s) == sorted(t))