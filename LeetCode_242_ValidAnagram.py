
    
def solution(s, t):
    s_new = s[:]
    for letter in t:
        if (letter in s and (len(s) == len(t))):
            s_new = s_new.replace(letter, '', 1)
    return s_new == ''

print(solution('abb', 'abbb'))