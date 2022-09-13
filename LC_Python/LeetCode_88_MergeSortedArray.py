
"""
def merge(nums1, m, nums2, n):

        for i in range(n):
            nums1[i + m] = nums2[i]
        nums1.sort()

print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))

"""
 #OR

def merge(nums1, m, nums2, n):
    nums1_copy = nums1[:m] 
    
    p1 = 0
    p2 = 0
        
    for p in range(n + m):
        if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
            nums1[p] = nums1_copy[p1] 
            p1 += 1
        else:
            nums1[p] = nums2[p2]
            p2 += 1
    return nums1
    
print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))