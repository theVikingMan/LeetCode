
    
def solution(ransomNote, magazine):
    numRansomNote = len(ransomNote)
    for letter in magazine:
        if (letter in ransomNote and numRansomNote > 0):
            ransomNote = ransomNote.replace(letter, "",1)
            numRansomNote -= 1        
    return numRansomNote == 0

print(solution('agg', 'efjbdg'))