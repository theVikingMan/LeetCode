import collections

def checkValid(matrix):
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            num = matrix[r][c]
            if num in rows[r] or num in cols[c]:
                return False
            rows[r].add(num)
            cols[c].add(num)

    return True

print(checkValid([[2,3,1],[1,2,3],[3,1,2]]))