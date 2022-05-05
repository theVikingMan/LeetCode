
# ------------ STEPS ------------ #
# Create an array of empty buckets;
# Put all array elements into the buckets;
# Sort each bucket;
# Go through all the buckets in order and build the fully sorted array.

def InsertionSort(bucket):
    for i in range (1, len (bucket)):
        var = bucket[i]
        j = i - 1
        while (j >= 0 and var < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var

def BucketSort(arr):
    max_val = max(arr)
    arrayLength = len(arr)

    size = max_val / arrayLength + 1 # calculate the size of each bucket
    buckets_list= [[] for x in range(arrayLength + 1)]

    for i in range(arrayLength):
        j = int(arr[i] / size)
        buckets_list[j].append(arr[i])

    for z in range(arrayLength):
        InsertionSort(buckets_list[z])

    sorted = []
    for x in range(arrayLength):
        sorted = sorted + buckets_list[x]
    return sorted

arr = [45,22,65,78,9,23,89,52]

print("Before Sorted: ", arr)
print("After Sorted: ", BucketSort(arr))