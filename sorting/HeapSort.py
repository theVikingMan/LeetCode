import heapq

def heapSort(array):
    res = []
    heapq.heapify(array)
    while array:
        val = heapq.heappop(array)
        res.append(val)
    return res

print(heapSort([1,4,2,7,5,4,2,9,1]))

# T: O(n * log(n)) --> O(log(n)) to heapify and O(n) to run through all numbers
# S: O(1) -> if result varibable isn't extra space