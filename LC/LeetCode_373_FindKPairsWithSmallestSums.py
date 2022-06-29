import heapq

def kSmallestPairs(self, nums1, nums2, k):
    # heapify the first row -> takes care of the edge case of always wondering about the
    # first row pointer being in-bounds
    # sum, first row pointer, second row pointer
    heap = [[nums1[i]+nums2[0], i, 0] for i in range(len(nums1)) ]
    heapq.heapify(heap)
    ans = []

    # either we have more elements to add or we dont have any more at all in the heap
    while k > 0 and len(heap) > 0:
        # Grab the min-most pair
        sumNum, first, second = heapq.heappop(heap)
        # Add the pair to result variable
        ans.append([nums1[first], nums2[second]])
        # Keep us from going out of bounds for the second row
        if second < len(nums2) - 1:
            heapq.heappush(heap, [nums1[first]+nums2[second + 1], first, second + 1])
        k-=1
    return ans

print(kSmallestPairs([1,7,11], [2,4,6],3))