from collections import Counter
import itertools

def largestVariance(s):
    counter = Counter(s)
    res = 0
    for a,b in itertools.permutations(counter, 2): # go through all pairs of letters
        # algo is based on Kadens (max subarray but maxing variance instead of sum)
        max_subarray = 0
        has_a, has_b = False, False
        remain_a, remain_b = counter[a], counter[b] # make copies, will be modifying
        for ch in s:
            if ch != a and ch != b: # not counting to the variance pair, dont include
                continue
            # start over the max sum as the variance dips below 0 (kaden's algo property)
            if max_subarray < 0 and remain_a != 0 and remain_b != 0:
                max_subarray = 0
                has_a, has_b = False, False
            if ch == a:
                max_subarray += 1
                remain_a -= 1
                has_a = True
            elif ch == b:
                max_subarray -= 1
                remain_b -= 1
                has_b = True
            if has_a and has_b:
                res = max(res, max_subarray)
    return res

print(largestVariance("aababbbc"))