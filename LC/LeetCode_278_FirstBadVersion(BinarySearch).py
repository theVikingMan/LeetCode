
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

def firstBadVersion(n):
    r = n-1
    l = 0
    while(l <= r):
        mid = l + (r - l) // 2
        if isBadVersion(mid) == False:
            l = mid+1
        else:
            r = mid-1
    return l

print(firstBadVersion(5, 2))